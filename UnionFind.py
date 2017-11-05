class UnionFind(object):
	"""
	While instaniating send an array of nodes
	"""
	def __init__(self,x):
		n =len(x)
		self.leader = {}
		for i in range(n):
			self.leader[x[i]] = x[i] #correct this 

	def __leader(self,node):
		return self.leader[node]

	def __changeLeader(self,key,leader):
		self.leader[key] = leader

	def Find(self,node):
		return self.leader[node]

	def Union(self,node1,node2):
		leader1,leader2 = __leader(node1),__leader(node2)
		for key in self.leader.keys():
			if(__leader(key)==leader2):
				__changeLeader(key,leader1)
	def PrintVertices(self):
		for key in self.leader.keys():
			print ("Key, Value = ",key," ",self.leader[key])

			