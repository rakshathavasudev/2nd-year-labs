n=10
t=[[1,3],[ 1,6],[1,3],[4,6],[4,10],[8,12],[8,12],[11,15],[13,15],[13,15]]
t.sort()
group=[]
new=[]
group.append(new)
group[0].append(t[0])
print(group)
for i in range(1,n):
	flag=False
	x=t[i]
	for j in range(len(group)):
		y=group[j][-1][1]
		if(x[0]>y):
			group[j].append(x)
			flag=True
			break
	if flag==False:
			new=[]
			new.append(x)
			group.append(new)
print("Minimum group of resources:",len(group))
for i in range(len(group)):
	print("Resource",i+1,":",end=' ')
	for j in range(len(group[i])):
		print(group[i][j],end=' ')
	print()