"""-----------------------------------------------------------------------------
----------------------------------class Message---------------------------------
--------------------------------------------------------------------------------
1.- Init function.
-----------------------------------------------------------------------------"""
from struct import*

class Message:
    def __init__(self,ID):
        self.MyID=ID
        self.Type='2'
        self.length_message=7
        self.dstID=''
        self.Len_msj=0
        self.msj=''
        self.crc=0

    def Message_pack(self,IDdst):
        pass
