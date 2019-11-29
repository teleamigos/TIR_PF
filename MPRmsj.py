"""-----------------------------------------------------------------------------
----------------------------------class MPRmsj----------------------------------
--------------------------------------------------------------------------------
1.- Init function.
2.- MPRmsj_pack.
3.- MPRmsj_unpack.
-----------------------------------------------------------------------------"""
from struct import*
import binascii
#import zlib

class MPRmsj:
    def __init__(self,ID):
        self.MyID=ID
        self.Type='1'
        self.MyMPR=[]
        self.crc=0
        self.msj_out=b''

    def MPRmsj_pack(self,tp):
        self.MyMPR=tp.MyMPR
        self.msj_out=self.Type.encode('utf-8')
        self.msj_out+=self.MyID.encode('utf-8')
        l=len(self.MyMPR)
        self.msj_out+=pack('!H',l)
        for n in self.MyMPR:
            self.msj_out+=n.encode('utf-8')
        #self.crc=zlib.crc32(self.msj_out)
        self.crc=binascii.crc32(self.msj_out)
        self.msj_out+=pack('!I',self.crc)
        print(self.msj_out)
        return self.msj_out

    def MPRmsj_unpack(self,msj_MPR,Tp):
        lista=[]
        num_MPR=unpack('!H',msj_MPR[2:4])[0]
        MPRs=msj_MPR[4:4+num_MPR]
        for i in range(o,num_MPR):
            m=MPRs[i:i+1]
            m=m.decode('utf-8')
            lista.append(m)
        if Tp.MyID in lista:
            Tp.SOYMPR=1
            print("Felicidades eres MPR HDP")
