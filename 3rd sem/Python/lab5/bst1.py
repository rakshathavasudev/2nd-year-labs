class treeNode:
	def __init__(self,val,left,right,parent):
		self.val=val
		self.leftChild=left
		self.rightChild=right
		self.parent=parent
class binTree:
	def __init__(self):
		self.root=None
	def tree_insert(self,tnode,node):
		if tnode.val<=node.val:
			if tnode.rightChild==None:
				tnode.rightChild=node
				node.parent=tnode
			else:
				self.tree_insert(tnode.rightChild,node)
		else:
			if tnode.leftChild==None:
				tnode.leftChild=node
				node.parent=tnode
			else:
				self.tree_insert(tnode.leftChild,node)



	def insert(self,val):
		node=treeNode(val,None,None,None)
		if self.root==None:
			self.root=node
		else:
			self.tree_insert(self.root,node)
	def search(self,node,val):
		if node==None:
			return None
		if node.val==val:
			return node
		elif node.val<=val:
			return self.search(node.rightChild,val)
		else:
			return self.search(node.leftChild,val)

	def minimum(self,node):
		
		if node.leftChild==None:
			return node
		else:
			return self.minimum(node.leftChild)
	def maximum(self,node):
		
		if node.rightChild==None:
			return node
		else:
			return self.maximum(node.rightChild)
	def successor(self,node):
		if node.rightChild!=None:
			return self.minimum(node.rightChild)
		else:
			p=node.parent
			child=node
			while p!=None and p.leftChild!=child :
				print(1)
				child=p
				p=p.parent
			if p==None:
				return None
			else:
				return p
	def predecessor(self,node):
		if node.leftChild!=None:
			return self.maximum(node.leftChild)
		else:
			p=node.parent
			child=node
			while p!=None and p.rightChild!=child :
				
				child=p
				p=p.parent
			if p==None:
				return None
			else:
				return p
	def delete(self,node):
		if node.leftChild==None and node.rightChild==None:
			if node.parent!=None:
				if node.parent.leftChild==node:
					node.parent.leftChild=None
				else:
					node.parent.rightChild=None
			else:
				self.root=None

		elif node.leftChild==None:
			if node.parent!=None:
				if node.parent.leftChild==node:
					node.parent.leftChild=node.rightChild
					node.rightChild.parent=node.parent
				else:
					node.parent.rightChild=node.rightChild
					node.rightChild.parent=node.parent
			else:
				self.root=node.rightChild

		elif node.rightChild==None:
			if node.parent!=None:
				if node.parent.leftChild==node:
					node.parent.leftChild=node.leftChild
					node.leftChild.parent=node.parent
				else:
					node.parent.rightChild=node.leftChild
					node.leftChild.parent=node.parent
			else:
				self.root=node.leftChild
		else:
			temp=self.successor(node)
			tempnode=node
			self.delete(temp)
			temp.leftChild=node.leftChild
			temp.rightChild=node.rightChild
			temp.parent=node.parent
			node.leftChild.parent=temp
			if node.rightChild!=None:
				node.rightChild.parent=temp
			if node.parent!=None:
				if node==node.parent.leftChild:
					node.parent.leftChild=temp
				else:
					node.parent.rightChild=temp
			else:
				self.root=temp




	def preorder(self,node):
		if node==None:
			return
		else:
			print(node.val)
			if node.leftChild!=None:
				self.preorder(node.leftChild)
			if node.rightChild!=None:
				self.preorder(node.rightChild)
	def height(self,node):
		if node==None:
			return 0
		else:
			return max(self.height(node.leftChild),self.height(node.rightChild))+1
	def printlevel(self,level):
		if level==1:
			print()
	def levelorder(self,node):
		h=self.height(self.root)
		for i in h:
			self.printLevel(i+1)



def main():
	Mytree=binTree()
	Mytree.insert(5)
	Mytree.insert(6)
	Mytree.insert(3)
	Mytree.insert(2)
	Mytree.insert(8)
	Mytree.insert(7)
	Mytree.insert(4)
	Mytree.preorder(Mytree.root)
	if Mytree.search(Mytree.root,4)!=None:
		print("4 found")
	else:
		print("Not found")
	
	print('Minimum element :',Mytree.minimum(Mytree.root).val)
	print('Maximum element :',Mytree.maximum(Mytree.root).val)
	print('Successor of 4 is',Mytree.successor(Mytree.search(Mytree.root,4)).val)
	print('Predecessor of 4 is ',Mytree.predecessor(Mytree.search(Mytree.root,4)).val)
	Mytree.delete(Mytree.search(Mytree.root,6))
	Mytree.preorder(Mytree.root)
	print("Height of tree",Mytree.height(Mytree.root))



if __name__ == '__main__':
    main()