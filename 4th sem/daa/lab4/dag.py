from collections import defaultdict
class Graph:
	def __init__(self,v):
		self.graph=defaultdict(list)
		self.v=v

	def addEdge(self,u,v):
		self.graph[u].append(v)

	def dagutil(self,v,visited,stack):
		visited[v]=True

		for i in self.graph[v]:
			if visited[i]==False:
				self.label+=1
				self.dagutil(i,visited,stack)
		stack.insert(0,v)
		return self.label


	def dag(self):
		self.label=0
		c=0
		visited=[False]*self.v
		stack=[]
		for i in range(self.v):
			if visited[i]==False:
				c+=self.dagutil(i,visited,stack)

		print(stack)
		print(c)

def main():
	g=Graph(6)
	g.addEdge(5, 2); 
	g.addEdge(5, 0); 
	g.addEdge(4, 0); 
	g.addEdge(4, 1); 
	g.addEdge(2, 3); 
	g.addEdge(3, 1); 
  
	g.dag()

main()



if (!isset($_SESSION['email'])) {
    header('location: ');
}