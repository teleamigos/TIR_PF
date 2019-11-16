"""-----------------------------------------------------------------------------
----------------------------------class Hello-----------------------------------
--------------------------------------------------------------------------------
1.- Init function.
-----------------------------------------------------------------------------"""
from struct import*
import zlib

class Hello:
    def __init__(self,ID):
        self.MyID=ID
        self.Type=0
        self.length_message=7
        self.dstID=0
        self.Length_nei=0
        self.NeighborList=[]
        self.crc=0
        self.msj_out=b''

    def Hello_pack(self,IDdst):
        self.dstID=IDdst
        self.msj_out=pack('!BBHB',self.dstID,self.Type,self.length_message,self.MyID)
        self.Length_nei=len(self.NeighborList)
        self.msj_out+=pack('!H',self.Length_nei)
        for Neighbor in self.NeighborList:
            self.msj_out += pack('!B',Neighbor)
        self.crc=zlib.crc32(self.msj_out)
        self.msj_out+=pack('!I',self.crc)
        return self.msj_out

    def Hello_unpack(self,msj_Hello):
        new_neighbor=unpack('!B',msj_Hello[4:5])[0]
        Len_nei=unpack('!H',msj_Hello[5:7])[0]
        if new_neighbor not in self.NeighborList:
            self.NeighborList.append(new_neighbor)
