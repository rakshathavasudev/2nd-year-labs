import heapq
class Node:
	def __init__(self,fr=None,sy=None,left=None,right=None):
		self.fr=fr
		self.sy=sy
		self.left=left
		self.right=right
	def __lt__(self,other):   #inbuilt function for comparing 2 nodes based on a parameter   def __eq__(self,other) for equal
		if self.fr<other.fr:
			return True
		else:
			return False

def huffman(s,f):
	h=[]
	for i in range(len(s)):
		node=Node(f[i],s[i],None,None)
		h.append(node)
	heapq.heapify(h) 
	for i in range(len(h)-1):
		t1=heapq.heappop(h)
		#print("t1:",t1.sy," ",t1.fr)
		t2=heapq.heappop(h)
		#print("t2:",t2.sy," ",t2.fr," sum:",t1.fr+t2.fr)
		node=Node(t1.fr+t2.fr,None,t1,t2)
		heapq.heappush(h,node)
	root=heapq.heappop(h)
	global r
	r=root
	#print("root:",root.sy)
	a=[]
	top=0
	pr(root,a,top)
def pr(root,a,top):
		if(root.left):
			a.insert(top,1)
			pr(root.left,a,top+1)
		if(root.right):
			a[top]=0
			pr(root.right,a,top+1)
		if(root.sy!=None):
			print(root.sy,":",end='')
			for i in range(top):
				print(a[i],"",end='')
			print()

def decoder(root,a):
	for i in range(len(a)):
		if a[i]=='1':
			root=root.right
		if a[i]=='0':
			root=root.left
		if root.sy!=None:
			print("the symbol is:",root.sy)
			break

def main():
	s=['a','b','c','d','e','f']
	f=[20,12,10,8,4,3]
	print("the huffman codes are:")
	print()
	huffman(s,f)
	print()
	print("decoding the huffman code:")
	print()
	file=open("f.txt","r")
	for line in file:
		decoder(r,line)

if __name__=='__main__':
	main()