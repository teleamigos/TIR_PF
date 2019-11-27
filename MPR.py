class MPR():
	def __init__(self):
		#self.vecinos = {'1':['0','2','3'],'2':['0','1','3']} #Para nodo 0
		#self.vecinos = {'0':['1','2'],'2':['0','1','3'], '3':['1','2','4']} #Para nodo 1
		#self.vecinos = {'0':['1','2'],'1':['0','2','3'],'3':['1','2','4']} #Para nodo 2
		#self.vecinos = {'1':['0','2','3'],'2':['0','1','3'],'4':['3','5']} #Para nodo 3
		self.vecinos = {'3':['1','2','4'], '5':['4']} #Para nodo 4
		#self.vecinos = {'4':['3','5']} #Para nodo 5
		self.id = '4'
		self.nei = []
		self.around = []
		self.MPR = []

	def k_MPR(self):
		for i in self.vecinos:
			self.nei.append(i)
		for i in self.vecinos:
			for j in self.vecinos[i]:
				try:
					self.around.index(j)
				except:
					self.around.append(j)
		self.around.sort()
		self.around.remove(self.id)
		#print(self.nei)
		#print(self.around)

		for i in self.nei:
			try:
				self.around.remove(i)
			except:
				print("")
		#print(self.around)

		for k in self.around:
			for i in self.vecinos:
				for j in self.vecinos[i]:
					if k == j:
						self.MPR.append(i)
		print(self.MPR)




MPR = MPR()
MPR.k_MPR()



