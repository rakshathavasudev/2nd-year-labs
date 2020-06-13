class Binaryheap:
	def __init__(self):
		self.heaplist=[""]
		self.size=0

	def insert(self,k):
		self.heaplist.append(k)
		self.size+=1
		self.swap(self.size)

	def buildheap(self,list):
		self.heaplist=[""]+list[:]
		self.size=len(self.heaplist)
		i=self.size//2
		while i>0:
			self.swap(i)
			i=i-1

	def swap(self,i):
		while i//2 > 0:
			if self.heaplist[i]>self.heaplist[i//2]:
				temp=self.heaplist[i//2]
				self.heaplist[i//2]=self.heaplist[i]
				self.heaplist[i]=temp
				self.swap(i-1)
			i=i//2

	def maximum(self):
		return self.heaplist[1]

	def extract_max(self):
		s=self.heaplist[1]
		self.heaplist[1]=self.heaplist[self.size]
		del self.heaplist[self.size]
		self.size-=1
		self.swap(self.size)
		return s
	
	def printlist(self):
		print(*self.heaplist)



def main():
	b=Binaryheap()
	b.buildheap([1,2])
	b.insert(8)
	b.insert(2)
	b.insert(10)
	b.insert(9)
	b.printlist()
	a=b.maximum()
	print("The maximum element is:")
	print(a)
	c=b.extract_max()
	print("The list after removing the max element i.e,",c,"is:")
	b.printlist()



main()
