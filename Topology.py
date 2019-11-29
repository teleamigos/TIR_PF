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
        self.MyMPR=[]
        self.SOYMPR=0

    def MPR(self):
    	for i in self.Topology:
    		self.nei.append(i)
    		for j in self.Topology[i]:
    			try:
    				self.around.index(j)
    			except:
    				self.around.append(j)
    	self.around.sort()
    	self.around.remove(self.id)
    	for i in self.nei:
    		try:
    			self.around.remove(i)
    		except:
    			time.sleep(0.05)

    	#print(self.nei)
    	#print(self.around)

    	aux = 0
    	for k in self.around:
    		for i in self.Topology:
    			for j in self.Topology[i]:
    				if k == j and aux == 0:
    					try:
    						self.MPR.index(i)
    					except:
    						self.MPR.append(i)
    						aux = 1
    		aux = 0
    	print("Los MPR's del nodo " + self.id + " son:")
    	print(self.MPR)
