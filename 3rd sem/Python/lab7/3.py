from collections import defaultdict
class Graph:

	def __init__(self):
		self.graph=defaultdict(list)

	def addedge(self,x,y):
		self.graph[x].append(y)
		self.graph[y].append(x)

	def components(self,v):
		self.label=0
		self.c=[0] * v
		for i in range(len(self.c)):
			if self.c[i]==0:
				self.label+=1
				self.bfs(i)					
		return self.label


	def bfs(self,s):
		print("\n")
		#self.label+=1
		visited=[False]*(len(self.graph))
		queue=[]
		queue.append(s)
		visited[s]=True

		while queue:
			s=queue.pop(0)
			print(s,end=" ")
			self.c[s]=self.label
			
			for i in self.graph[s]:
				if visited[i]==False:
					queue.append(i)
					visited[i]=True
		
			

def main():
	print("Enter the no. of vertices")
	v=int(input())
	g=Graph()
	print("Enter the no. of edges")
	e=int(input())
	print("Enter the edges")
	for i in range(e):
		x,y=input().split()
		g.addedge(int(x),int(y))
	z=g.components(v)
	print("\n")
	print("The no. of components are:",z)





main()