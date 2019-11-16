"""-----------------------------------------------------------------------------
----------------------------------Main------------------------------------------
--------------------------------------------------------------------------------
1.- Init variables.
"""
from Packed import*
import time
from threading import Thread
#from socket import socket, AF_PACKET, SOCK_RAW, htons

#s=socket(AF_PACKET,SOCK_RAW,htons(0x0801))
#s.bind(("",0))
pack=Packed(b'\x94\x53\x30\x44\xca\x7f','0')
pack2=Packed(b'\x94\x53\x30\x44\xca\x7f','1')
print('Your user ID : ', pack.tp.MyID)
print('Your MAC addres : ',pack.myMACadd)
msj=pack2.Pack('0','b')
while True:
    out=pack.Pack('0','b')
    """Thread1=Thread(target=Send,args=(out,s))
    Thread1.start()
    Thread1.join()
    msj=s.recv(1024)"""
    if not msj:
        print("Not received...")
        break
    pack.Unpack(msj)
