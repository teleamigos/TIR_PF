"""-----------------------------------------------------------------------------
----------------------------------class MPRmsj----------------------------------
--------------------------------------------------------------------------------
1.- Init function.
2.- MPRmsj_pack.
3.- MPRmsj_unpack.
-----------------------------------------------------------------------------"""
from struct import*
import zlib

class MPRmsj:
    def __init__(self,ID):
        self.MyID=ID
        self.Type='1'
        self.length_message=10
        self.dstID=''
        self. MyMPR=''
        self.crc=0
        self.msj_out=b''

    def MPRmsj_pack(self,IDdst,tp):
        self.MyMPR=tp.MyMPR
        self.dstID=IDdst
        self.NeighborList=tp.Neighbors
        self.msj_out=self.Type.encode('utf-8')+self.dstID.encode('utf-8')
        self.msj_out+=pack('!H',self.length_message)+self.MyID.encode('utf-8')
        self.msj_out+=self.MyMPR.encode('utf-8')
        self.crc=zlib.crc32(self.msj_out)
        self.msj_out+=self.crc
        return self.msj_out

    def MPRmsj_unpack(self,msj_MPR,Tp):
        IDsrc=msj_MPR[4:5].decode('utf-8')
        IDmpr=msj_MPR[5:6].decode('utf-8')
        Tp.MPRs[IDsrc]=IDmpr
