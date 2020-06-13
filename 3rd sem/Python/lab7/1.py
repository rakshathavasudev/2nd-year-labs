class Graph:

	def __init__(self,size):
		self.adj=[]
		for i in range(size):
			self.adj.append([0 for i in range(size)])
		self.size=size


	def addedge(self,x,y):
		if x==y:
			{}
		self.adj[x][y]=1
		self.adj[y][x]=1


	def matrix(self):
		for i in range(self.size):
			for j in range(self.size):
				print(self.adj[i][j]," ",end=" ")
			print("\n")	

class listnode:
	def __init__(self,val):
		self.val=val
		self.next=None

class linkedlist:
	def __init__(self,v):
		self.v=v
		self.list=[None] * self.v

	def add(self,x,y):
		node=listnode(x)
		node.next=self.list[y]
		self.list[y]=node

		node=listnode(y)
		node.next=self.list[x]
		self.list[x]=node

	def adjlist(self):
		for i in range(self.v):
			print("Vertex",i,":",end=" ")
			temp=self.list[i]
			while temp:
				print("{}".format(temp.val),end=" ")
				temp=temp.next
			print("\n")		


def main():
	print("Enter the no. of vertices")
	v=int(input())
	g=Graph(v)
	l=linkedlist(v)
	print("Enter the no. of edges")
	e=int(input())
	print("Enter the edges")
	for i in range(e):
		x,y=input().split()
		g.addedge(int(x),int(y))
		l.add(int(x),int(y))
	g.matrix()
	l.adjlist()

main()
