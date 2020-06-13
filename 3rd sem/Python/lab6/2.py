class Binaryheap:
    def __init__(self):
        #self.heaplist=[""]
        self.size=0

    def buildheap(self,list):
        i=len(list)//2
        self.size=len(list)
        #print(*self.heaplist)
        while(i>0):
            self.heapify(list,i,self.size)
            i=i-1
        #print(*list)

    def heapify(self,arr,i,n):
        l=2 * i +1 
        r=2 * i +2

        if l<n and arr[l]>arr[i]:
            largest=l
        else:
            largest=i
        
        if r<n and arr[r]>arr[largest]:
            largest=r
        if largest!=i:
            temp=arr[i]
            arr[i]=arr[largest]
            arr[largest]=temp
            self.heapify(arr,largest,n)
            #print(*arr)

    def printlist(self,list):
        print(*list)






def main():
    b=Binaryheap()
    b.buildheap([1,2,3,4,5])
    #b.printlist(list1)

main()