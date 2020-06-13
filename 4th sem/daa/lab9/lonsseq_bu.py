def subseq(a,n,lis,ans):
	for i in range(n):
		for j in range(i+1,n):
			if a[i]<a[j] and lis[i]>lis[j]+1:
				lis[i]=lis[j]+1
				ans[i]=j
		mx=i
	return mx

def main():
	a=[5,2,8,6,3,6,9,7]
	#a=[3,10,2,1,20]
	n=len(a)
	lis=[1]*n
	ans=[-1]*n
	mx=subseq(a,n,lis,ans)
	print(mx)
	print(lis)
	x=[]
	print("the answer is:",max(lis))
	while mx>=0:
		x.append(a[mx])
		mx=ans[mx]
	for i in range(len(x)-1,-1,-1):
		print(x[i]," ",end='')
	print()

if __name__=='__main__':
	main()