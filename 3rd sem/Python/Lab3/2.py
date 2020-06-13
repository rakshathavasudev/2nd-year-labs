class LinkedList:
    """Defines a Singly Linked List.

    attributes: head
    """
    
    def __init__(self):
        """Create a new list with a Sentinel Node"""
        self.head=ListNode()
        
        

    def insert(self,x,pos):
        """Insert element x in the position after pos"""
        temp=ListNode(x)
        temp.next=pos.next
        pos.next=temp

    def delete(self,pos):
        """Delete the node following node pos in the linked list."""
        if pos.next!=None:
            pos.next=pos.next.next

    def print(self):
        """ Print all the elements of a list in a row."""
        ref=self.head
        ref=ref.next
        if ref==None:
            print('No elements')
        while ref!=None:
            print(ref.value,end=' ')
            ref=ref.next

    def insertAtIndex(self,x,i):
        """Insert value x at list position i. (The position of the first element is taken to be 0.)"""
        temp=ListNode(x)
        pos=None
        ref=self.head
        while  ref!=None:
            if pos==i:
                temp=ListNode(x)
                temp.next=pos.next
                pos.next=temp
                
        ref=ref.next
        pos=pos+1
        

        

    def search(self, x):
        """Search for value x in the list. Return a reference to the first node with value x; return None if no such node is found."""
        ref=self.head
        ref=ref.next
        while ref!=None:
            if ref.value==x:
                print('The value is found')



    def len(self):
        """Return the length (the number of elements) in the Linked List."""
        r=0
        ref=self.head.next
        while  ref!=None:
            r=r+1
            ref=ref.next
        return(r)

    def isEmpty(self):
        """Return True if the Linked List has no elements, False otherwise."""
        c=0
        ref=self.head
        while  ref!=None:
            c=c+1
            ref=ref.next
        if c==0:
            return(True)
        return(False)

class ListNode:
    """Represents a node of a Singly Linked List.

    attributes: value, next. 
    """

    def __init__(self,val=None,nxt=None):
        self.value=val
        self.next=nxt

def main():
    L = LinkedList()
    L.head=ListNode(5)
    L.insert(10,L.head)
    print('List is: ',end=' ')
    L.print()
    L.insert(12,L.head.next)
    print('\nList is: ',end=' ')
    L.print()
    L.insert(2,L.head)
    print('\nList is: ',end=' ')
    L.print()
    a=L.len()
    print('\nSize of L is ',a,end=' ')
    L.delete(L.head)
    print('\nList is: ',end=' ')
    L.print()
    L.delete(L.head.next)
    print('\nList is: ',end=' ')
    L.print()
    c=L.isEmpty()
    print('\nList is empty?',c,end=' ')
    d=L.len()
    print('\nSize of L is ',d,end=' ')
    L.delete(L.head)
    x=L.isEmpty()
    print('\nList is empty?',x,end=' ')
    y=L.len()
    print('\nSize of L is ',y,end=' ')
    L.insertAtIndex(2,0)
    L.insertAtIndex(1,0)
    L.insertAtIndex(4,2)
    L.insertAtIndex(3,2)
    print('\nList is: ',end=' ')
    L.print()

if __name__=='__main__':
    main()

