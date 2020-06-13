class minheap:

	#edited to perform operations on the key of a key,value pair

	def __init__(self,array):
		if array==None:
			self.elements = []
			self.capacity = 0
		else:
			self.elements = array
			self.capacity = len(array)
		
	def left(self,i):
		return int((2*i)+1)
	def right(self,i):
		return int((2*i)+2)
	def parent(self,i):
		return int(0.5*i)
	def maximum(self):
		return self.elements[0][0]

	def swap(self,i,j):
		temp = self.elements[i][0]
		self.elements[i][0] = self.elements[j][0]
		self.elements[j][0] = temp

	def insert(self,key,value):
		pair = [key,value]
		self.elements.append(pair)
		self.capacity = self.capacity + 1

		i = self.capacity - 1
		j = self.parent(i)
		
		while self.elements[i][0] < self.elements[j][0]:
			self.swap(i,j)
			i = j
			j = self.parent(i)

	def delete(self):
		self.elements[0] = self.elements.pop()
		self.capacity = self.capacity - 1
		i = 0
		j = self.left(i)
		k = self.right(i)

		n = self.capacity
		while i<n:
			if j<n and self.elements[i][0] > self.elements[j][0]:
				self.swap(i,j)
				i = j
				j = self.left(i)
				k = self.right(i)
			elif k<n and self.elements[i][0] > self.elements[k][0]:
				self.swap(i,k)
				i = k
				j = self.left(i)
				k = self.right(i)
			else:
				break

	def heapify(self,n,i):
		#start from i, keep going down until heap condition satisfied
		smallest = i
		l = self.left(i)
		r = self.right(i)
		if l < n and self.elements[i][0] > self.elements[l][0]: 
			smallest = l 
		if r < n and self.elements[smallest][0] > self.elements[r][0]: 
			smallest = r
		if smallest != i: 
			self.swap(i,smallest)
			self.heapify(n,smallest) 

	def buildheap(self):
		#examine from the bottom row, make them all heaps
		n = self.capacity
		for i in (int(0.5*n)-1,-1,-1):
			self.heapify(n,i)

	def extractmin(self):
		min1 = self.elements[0][1] #returning the vertex value rather than distance
		
		if(len(self.elements) == 1):
			self.elements.pop(0)
			self.capacity = self.capacity - 1

		elif (self.elements[1][0] == 10000):
			# print("this is true no")
			self.elements.pop(0)
			self.capacity = self.capacity-1
			# print(self.elements,"debug3
		else:
			self.elements[0] = self.elements.pop()
			self.capacity = self.capacity - 1
			self.heapify(self.capacity,0)
			# print(self.elements,"debug32")



		return min1

	def heapsort(self):
		n = self.capacity
		self.buildheap()
		#Smallest item is root. Replace it with the last item of the heap followed by size--. Finally, heapify the root of tree
		#Repeat above steps while size of heap > 1
		for i in range(n-1, 0, -1): 
			self.swap(i,0)
			self.heapify(i,0) 

	def update_priority(self,v,dist):

		index = -1

		for list_iterator in self.elements:
			index = index + 1
			# print(list_iterator,"iterdebug")
			if (list_iterator[1] == v):
				# print("broken")
				break

		# print(index,"debug")
		self.elements[index][0] = dist
		
		self.buildheap()

	def isEmpty(self):

		if self.elements:
			return False

		return True


	def __str__(self):
		strs = ""
		for i in range(0,self.capacity):
			strs = strs + str(self.elements[i]) + " "
		return strs



class adjlist:
	def __init__(self,size):
		self.adjlist = [[] for i in range(0,size)]
		self.size = size
		self.edge_weight = [[0 for i in range(0,size)] for i in range(0,size)]
		self.distance = [10000 for i in range(0,size)]
		self.parent = [None for i in range(0,size)]

	def insert(self,i,j,weight):
		self.adjlist[i].append(j)
		self.adjlist[j].append(i)
		self.edge_weight[i][j] = weight
		self.edge_weight[j][i] = weight

	def contents(self):
		for i in range(0,self.size):
			print(self.adjlist[i], sep = ' ', end = '\n')

	def dijkstra(self,v):

		iterator = 0

		H = minheap(None)
		self.distance[v] = 0

		for j in range(0,self.size):
			H.insert(self.distance[j], j)

		

		while H.isEmpty()==False:
			w = H.extractmin()
			for k in self.adjlist[w]:

				if self.distance[k] > (self.distance[w] + self.edge_weight[w][k]):
					self.distance[k] = (self.distance[w] + self.edge_weight[w][k])

					if H.isEmpty()==False:
						H.update_priority(k,self.distance[k])

					self.parent[k] = w


		print("Distance from source vertex " + str(v))
		for i in range(0,self.size):
			if(self.distance[i]!=10000):
				print(i,":",self.distance[i])
			else:
				print(i,"infinity")





def main():
	n = int(input("Enter the no. of vertices: "))
	l = adjlist(n)

	n = int(input("Enter the no. of edges: "))

	print("Enter edges along with their weights")
	for it in range(0,n):
		strx = str(input()).split()

		i = int(strx[0])
		j = int(strx[1])
		k = int(strx[2])
		if k<0:
			print("weight should be positive")
			exit()
		if i>=n or j>=n:
			print("vertex does't exist")
			exit()
		l.insert(i,j,k)
	
	v = int(input("Enter the source vertex:"))
	# s = l.bfs(v)
	# str1 = ' '.join(str(j) for j in s)
	print("D-SPA on vertex yields:")
	l.dijkstra(v)

if __name__ == '__main__':
	main()
