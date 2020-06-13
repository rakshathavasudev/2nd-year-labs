from collections import defaultdict

class Graph:

	def __init__(self):
		self.graph=defaultdict(list)
		self.startime={}
		self.endtime={}
		self.time=0
		


	def addedge(self,x,y):
		self.graph[x].append(y)
		self.graph[y].append(x)

	
	def dfscon(self,s,visited):
		#time=0
		visited[s]=True
		#self.startime[s]=time+1
		print(s,end=" ")
		for i in self.graph[s]:
			if visited[i]==False:
				self.dfscon(i,visited)

	def dfs(self,s):
		visited=[False]*(len(self.graph))
		self.dfscon(s,visited)

	#time=0
	def timestamp1(self,s,visited):
		#time=0
		#global time
		visited[s]=True
		self.startime[s]=self.time+1
		self.time+=1
		#print(s,end=" ")
		for i in self.graph[s]:
			if visited[i]==False:
				#self.time+=1
				self.timestamp1(i,visited)
		self.endtime[s]=self.time+1
		self.time=self.time+1


	def timestamp(self,s):
		visited=[False]*(len(self.graph))
		#time=0
		self.timestamp1(s,visited)

	def printime(self,v):
		for i in range(v):
			string="Time stamp of {}:[{},{}]."
			print(string.format(i,self.startime[i],self.endtime[i]))



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
	print("The dfs traversal is:")
	g.dfs(s)
	g.timestamp(s)
	print("The time stamps:")
	g.printime(v)

if __name__ == '__main__':
	main()
