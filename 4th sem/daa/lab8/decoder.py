import heapq
class Node:
	def __init__(self,symb,freq,left,right):
		self.symb=symb
		self.freq=freq
		self.left=left
		self.right=right

	def __lt__(self,other):   
		if self.freq<other.freq:
			return True
		else:
			return False

def huffman(n,s,f):
	leaves=[]
	for i in range(n):
		node=Node(s[i],f[i],None,None)
		leaves.append(node)
	heapq.heapify(leaves)
	for i in range(len(leaves)-1):
		t1=heapq.heappop(leaves)
		t2=heapq.heappop(leaves)
		node=Node(None,t1.freq+t2.freq,t1,t2)

		heapq.heappush(leaves,node)
	root=heapq.heappop(leaves)
	global r
	r=root
	
	a=[]
	top=0
	print_f(root,a,top)

def print_f(root,a,top):
	if(root.left):
		a.insert(top,1)
		print_f(root.left,a,top+1)

	if(root.right):
		a.insert(top,0)
		print_f(root.right,a,top+1)

	if(root.symb!=None):
		print(root.symb,end=' ')
		for i in range(top):
			print(a[i],end=' ')
		print()

def decoder(root,a):
	for i in range(len(a)):
		if(a[i]=='0'):
			root=root.right

		if(a[i]=='1'):
			root=root.left

		if(root.symb!=None):
			print(root.symb)
			break
def main():
	n=6
	s=['a','b','c','d','e','f']
	f=[20,12,10,8,4,3]
	huffman(n,s,f)
	file=open('f.txt','r')
	for line in file:
		decoder(r,line)

main()
	

