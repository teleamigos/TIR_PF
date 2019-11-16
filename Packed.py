"""-----------------------------------------------------------------------------
----------------------------------class packed----------------------------------
--------------------------------------------------------------------------------
1.- Init function.
-----------------------------------------------------------------------------"""
from struct import*
from Hello import*
from MPRmsj import*
from Message import*

class Packed(Hello,MPRmsj,Message):
    def __init__(self,MyMacAdd):
        self.myMACadd=MyMacAdd
        self.MACadds={
        'A':b'',
        'B':b''
        }
        self.protocol=b'\x08\x01'
        self.payload=''
