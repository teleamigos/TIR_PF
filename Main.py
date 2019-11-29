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

s=socket(AF_PACKET,SOCK_RAW,htons(0x0801))
s.bind(("wlp1s0",0))
pack=Packed(b'\x94\x53\x30\x44\xca\x7f','0')
print('Your user ID : ', pack.tp.MyID)
print('Your MAC addres : ',pack.myMACadd)
tiempo = time.time()
tiempo2 = tiempo
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
