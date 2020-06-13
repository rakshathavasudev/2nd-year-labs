
class TreeNode(object): 
    def __init__(self, val): 
        self.val = val 
        self.left = None
        self.right = None
        self.parent=None
        self.height = 1

# AVL tree class which supports the 
# Insert operation 
class AVL_Tree(object): 

    def insert(self, root, key): 
    
        # Step 1 - Perform normal BST 
        if not root: 
            return TreeNode(key) 
        elif key < root.val: 
            root.left = self.insert(root.left, key) 
        else: 
            root.right = self.insert(root.right, key) 

        # Step 2 - Update the height of the 
        # ancestor node 
        root.height = 1 + max(self.getHeight(root.left), 
                        self.getHeight(root.right)) 

        # Step 3 - Get the balance factor 
        balance = self.getBalance(root) 

        # Step 4 - If the node is unbalanced, 
        # then try out the 4 cases 
        # Case 1 - Left Left 
        if balance > 1 and key < root.left.val: 
            return self.rightRotate(root) 

        # Case 2 - Right Right 
        if balance < -1 and key > root.right.val: 
            return self.leftRotate(root) 

        # Case 3 - Left Right 
        if balance > 1 and key > root.left.val: 
            root.left = self.leftRotate(root.left) 
            return self.rightRotate(root) 

        # Case 4 - Right Left 
        if balance < -1 and key < root.right.val: 
            root.right = self.rightRotate(root.right) 
            return self.leftRotate(root) 

        return root 

    def delete(self, root, key): 
  
        # Step 1 - Perform standard BST delete 
        if not root: 
            return root 
  
        elif key < root.val: 
            root.left = self.delete(root.left, key) 
  
        elif key > root.val: 
            root.right = self.delete(root.right, key) 
  
        else: 
            if root.left is None: 
                temp = root.right 
                root = None
                return temp 
  
            elif root.right is None: 
                temp = root.left 
                root = None
                return temp 
  
            temp = self.getMinValueNode(root.right) 
            root.val = temp.val 
            root.right = self.delete(root.right, 
                                      temp.val) 
  
        # If the tree has only one node, 
        # simply return it 
        if root is None: 
            return root 
  
        # Step 2 - Update the height of the  
        # ancestor node 
        root.height = 1 + max(self.getHeight(root.left), 
                            self.getHeight(root.right)) 
  
        # Step 3 - Get the balance factor 
        balance = self.getBalance(root) 
  
        # Step 4 - If the node is unbalanced,  
        # then try out the 4 cases 
        # Case 1 - Left Left 
        if balance > 1 and self.getBalance(root.left) >= 0: 
            return self.rightRotate(root) 
  
        # Case 2 - Right Right 
        if balance < -1 and self.getBalance(root.right) <= 0: 
            return self.leftRotate(root) 
  
        # Case 3 - Left Right 
        if balance > 1 and self.getBalance(root.left) < 0: 
            root.left = self.leftRotate(root.left) 
            return self.rightRotate(root) 
  
        # Case 4 - Right Left 
        if balance < -1 and self.getBalance(root.right) > 0: 
            root.right = self.rightRotate(root.right) 
            return self.leftRotate(root) 
  
        return root

    def getMinValueNode(self, root): 
        if root is None or root.left is None: 
            return root 
  
        return self.getMinValueNode(root.left) 
   


    def leftRotate(self, z): 

        y = z.right 
        T2 = y.left 

        # Perform rotation 
        y.left = z 
        z.right = T2 

        # Update heights 
        z.height = 1 + max(self.getHeight(z.left), 
                        self.getHeight(z.right)) 
        y.height = 1 + max(self.getHeight(y.left), 
                        self.getHeight(y.right)) 

        # Return the new root 
        return y 

    def rightRotate(self, z): 

        y = z.left 
        T3 = y.right 

        # Perform rotation 
        y.right = z 
        z.left = T3 

        # Update heights 
        z.height = 1 + max(self.getHeight(z.left), 
                        self.getHeight(z.right)) 
        y.height = 1 + max(self.getHeight(y.left), 
                        self.getHeight(y.right)) 

        # Return the new root 
        return y 

    def getHeight(self, root): 
        if not root: 
            return 0

        return root.height 

    def getBalance(self, root): 
        if not root: 
            return 0

        return self.getHeight(root.left) - self.getHeight(root.right) 

    def preOrder(self, root): 

        if not root: 
            return

        print("{0} ".format(root.val), end="") 
        self.preOrder(root.left) 
        self.preOrder(root.right) 

    def search(self,root,val):
        if root==None:
            return None
        if root.val==val:
            return root
        elif root.val<=val:
            return self.search(root.right,val)
        else:
            return self.search(root.left,val)

    def minimum(self,root):
        
        if root.left==None:
            return root
        else:
            return self.minimum(root.left)
    def maximum(self,root):
        
        if root.right==None:
            return root
        else:
            return self.maximum(root.right)
    '''def successor(self,node):
        if node.right!=None:
            return self.minimum(node.right)
        else:
            p=node.parent
            child=node
            while p!=None and p.left!=child :
                print(1)
                child=p
                p=p.parent
            if p==None:
                return None
            else:
                return p'''
    '''def predecessor(self,node):
        if node.left!=None:
            return self.maximum(node.left)
        else:
            p=node.parent
            child=node
            while p!=None and p.right!=child :
                print(1)
                child=p
                p=p.parent
            if p==None:
                return None
            else:
                return p'''


# Driver program to test above function 
myTree = AVL_Tree() 
root = None

root = myTree.insert(root, 10) 
root = myTree.insert(root, 20) 
root = myTree.insert(root, 30) 
root = myTree.insert(root, 40) 
root = myTree.insert(root, 50) 
root = myTree.insert(root, 25) 

# Preorder Traversal 
print("The tree is:") 
myTree.preOrder(root) 
print()
print("Enter the element to be searched")
s=int(input())
if myTree.search(root,s)!=None:
    print("Element found")
else:
    print("Not found")
    
print('Minimum element :',myTree.minimum(root).val)
print('Maximum element :',myTree.maximum(root).val)
'''print("Enter the element whose successor is to be found")
S=int(input())
print('Successor of the element is:',myTree.successor(myTree.search(root,S)).val)'''
print("Enter the element to be deleted")
k=int(input())
root=myTree.delete(root,k)
print("The tree after deletion is:")
myTree.preOrder(root)
print()
#print('Predecessor of the element is :',myTree.predecessor(myTree.search(root,P)).val) 

# This code is contributed by Ajitesh Pathak 
