"""-----------------------------------------------------------------------------
----------------------------------Class Topology--------------------------------
--------------------------------------------------------------------------------
1.- Init
-----------------------------------------------------------------------------"""

class Topology:
    def __init__(self,ID):
        self.MyID=ID
        self.Neighbors=[]
        self.Topology={}
        self.MyMPR=''
        self.MPRs=[]

    def MPR(self):
        aux=0
        i=0
        c=0
        lista=[]
        vecinos=[]
        for Node in self.Topology:
            if Node !='0':
                L=len(self.Topology[Node])
                lista.append((Node,L))
        for nodo in lista:
            c=0
            if nodo[1]>1:
                if len(vecinos)==0:
                    vecinos.append(self.Topology[nodo[0]])
                    self.MPRs.append(nodo[0])
                else:
                    for v in self.Topology[nodo[0]]:
                        if v in vecinos[0]:
                            pass
                        else :
                            vecinos[0].append(v)
                            c+=1
                    if c>1:
                        self.MPRs.append(nodo[0])
        """print(vecinos)"""
