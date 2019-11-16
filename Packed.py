"""-----------------------------------------------------------------------------
----------------------------------class packed----------------------------------
--------------------------------------------------------------------------------
1.- Init function.
-----------------------------------------------------------------------------"""
from struct import*
from Hello import*
from MPRmsj import*
from Message import*
from Topology import*

class Packed(Hello,MPRmsj,Message,Topology):
    def __init__(self,MyMacAdd):
        self.myMACadd=b'\x94\x53\x30\x44\xca\x7f'
        self.broadcast=b'\xff\xff\xff\xff\xff\xff'
        self.protocol=b'\x08\x01'
        self.payload=''
        self.Type_message={
        'Hello':'0',
        'MPR_message':'1',
        'Message':'2'
        }
        self.tp=Topology()
        self.msj_out=''
        self.message_Hello=Hello('0')
        self.messgae_MPR=MPRmsj('0')
        self.message=Message('0')

    def Pack(self,type,IDdst):
        self.msj_out=self.broadcast+self.myMACadd+self.protocol
        if type==self.Type_message['Hello']:
            self.payload=self.message_Hello.Hello_pack(IDdst,self.tp)
        elif type==self.Type_message['MPR_message']:
            self.payload=self.message_MPR.MPRmsj_pack(IDdst,self.tp)
        elif type==Type_message['Message']:
            self.payload=self.message.Message_pack(IDdst)
        else:
            print('Error, invalid type of message...')
        self.msj_out+=self.payload
        print(self.msj_out)
