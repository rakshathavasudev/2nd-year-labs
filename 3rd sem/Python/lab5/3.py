import time
from bst import binTree
from avl import AVL_Tree












def main():
	Mytree=binTree()
	start_time=time.time()
	with open('1000') as openfileobject:
		for line in openfileobject:
			Mytree.insert(int(line.strip('\n')))
	print("%s sec is the time taken for bst insertion of 1000 keys" % (time.time() - start_time))
	start_time=time.time()
	with open('1000') as openfileobject:
		for line in openfileobject:
			root = myTree.insert(root,int(line.strip('\n')))
	print("%s sec is the time taken for avl insertion of 1000 keys" % (time.time() - start_time))
	

if __name__=='__main__':
	main()