"""-----------------------------------------------------------------------------
----------------------------------class Hello-----------------------------------
--------------------------------------------------------------------------------
1.- Init function: default parameters, put yourself ID
2.- Hello_pack: Pack infor for Hello, put IDdst and ID. Returns a package of the
    info.
3.- Hello_unpack : Unpack and change topology information.
-----------------------------------------------------------------------------"""
from struct import*
import zlib
#from Topology import*

class Hello():
    def __init__(self,ID):
        self.MyID=ID
        self.Type='0'
        self.length_message=7
        self.dstID=''
        self.Length_nei=0
        self.NeighborList=[]
        self.crc=0
        self.msj_out=b''

    def Hello_pack(self,IDdst,tp):
        self.dstID=IDdst
        self.NeighborList=tp.Neighbors
        self.msj_out=self.Type.encode('utf-8')+self.dstID.encode('utf-8')
        self.msj_out+=pack('!H',self.length_message)+self.MyID.encode('utf-8')
        self.Length_nei=len(self.NeighborList)
        self.msj_out+=pack('!H',self.Length_nei)
        for n in self.NeighborList:
            self.msj_out+=n.encode('utf-8')
        self.crc=zlib.crc32(self.msj_out)
        self.msj_out+=pack('!I',self.crc)
        return self.msj_out


    def Hello_unpack(self,msj_Hello,Tp):
        src=msj_Hello[1:2].decode('utf-8')
        len_msj=len(msj_Hello)
        list=[]
        new_nei=msj_Hello[4:5].decode('utf-8')
        if new_nei not in self.NeighborList:
            self.NeighborList.append(new_nei)
            Tp.Neighbors=self.NeighborList
            len_nei=unpack('!H',msj_Hello[5:7])[0]
            nei_list=msj_Hello[7:7+len_nei]
            for i in range(0,len_nei):
                n=nei_list[i:i+1]
                n=n.decode('utf-8')
                list.append(n)
            Tp.Topology[new_nei]=list
