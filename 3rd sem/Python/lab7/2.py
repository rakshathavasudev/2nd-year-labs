from collections import defaultdict

class Graph:

	def __init__(self):
		self.graph=defaultdict(list)
		self.dist={}


	def addedge(self,x,y):
		self.graph[x].append(y)
		self.graph[y].append(x)

	def bfs(self,s):

		visited=[False]*(len(self.graph))
		queue=[]
		self.dist[s]=0
		queue.append(s)
		visited[s]=True

		while queue:
			s=queue.pop(0)
			print(s,end=" ")
			

			for i in self.graph[s]:
				if visited[i]==False:
					queue.append(i)
					visited[i]=True


	def distance(self,s):
		print("\n")

		visited=[False]*(len(self.graph))
		queue=[]
		self.dist[s]=0
		queue.append(s)
		visited[s]=True

		while queue:
			s=queue.pop(0)
			

			for i in self.graph[s]:
				if visited[i]==False:
					queue.append(i)
					visited[i]=True
					self.dist[i]=self.dist[s]+1
					string="The distance from {} to {} is:{}."
					print(string.format("source",i,self.dist[i]))
								
					
			

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
	print("Enter the source vertex")
	s=int(input())
	print("The bfs traversal is:")
	g.bfs(s)
	g.distance(s)

main()