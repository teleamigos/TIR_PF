"""-----------------------------------------------------------------------------
----------------------------------Main------------------------------------------
--------------------------------------------------------------------------------
1.- Init variables.
2.- Send Hello :
    * Get topology infomation.
    * Information is packed to be sent through broadcast.
3.- Receive Hello :
    * Information is unpacked.
    * Get Topology from neighbos.
    * Get neighbors.
4.- Compute MPR.
5.- Send MPR message :
    * The list of MPRs is sent through broadcast.
6.- Receive MPR message :
    *The message is unpacked
    *Get MPR list
    *If My node is in  MPR list, My node is MPR.
7.- Send Temperature message:
-----------------------------------------------------------------------------"""
from Packed import*
import time
from threading import Thread
from socket import socket, AF_PACKET, SOCK_RAW, htons
from Send import *

def Special_unapack(msj,tp,crcs):
    payload=msj[14:]
    type=payload[0:1].decode('utf-8')
    if type =='2':
        dst=msj[2:3].decode('utf-8')
        if dst !=tp.MyID:
            if tp.SOYMPR==1:
                steps=unapack('!B',msj[3:4])
                l=len(msj)
                crc=unpack('!I',msj[l-4:])
                if steps <3:
                    return crc
                elif crc in crcs:
                    return -1
                else :
                    return -1
            else:
                return -1 #We cannot do anything
        else:
            return 0 #unpack all the information using original functions

s=socket(AF_PACKET,SOCK_RAW,htons(0x0801))
s.bind(("wlp1s0",0))
pack=Packed(b'\x94\x53\x30\x44\xca\x7f','0')
print('Your user ID : ', pack.tp.MyID)
print('Your MAC addres : ',pack.myMACadd)
tiempo = time.time()
tiempo2 = tiempo
crcs=[]
while ((tiempo2-tiempo)<5):
    out=pack.Pack('0','b')
    Thread1=Thread(target=send,args=(out,s))
    Thread1.start()
    Thread1.join()
    msj=s.recv(1024)
    if not msj:
        print("Not Hello received...")
        break
    pack.Unpack(msj)
    tiempo2 = time.time()
pack.tp.MPR()#Compute MPR
while True:
    out=pack.Pack('1','b')
    Thread1=Thread(target=send,args=(out,s))
    Thread1.start()
    Thread1.join()
    msj=s.recv(1024)
    if not msj:
        print('Not MPR message received')
        break
    pack.Unpack(msj)

while True:
    msj=s.recv(1024)
    if not msj:
        print("Not temperature...")
        break
    ans=Special_unapack(msj,pack.tp,crcs)
    if ans !=-1 and ans !=0:
        print('re-transmitting...')
        crcs.append(ans)
        
    elif ans==-1:
        print("discard...")
    elif ans==0:
        print('unpacking...')
