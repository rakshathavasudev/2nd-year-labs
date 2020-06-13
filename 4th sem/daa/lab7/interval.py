n=8
t=[[1,3],[2,8],[2,5],[3,7],[4,8],[4,6],[6,12],[7,10]]
t.sort()
print(t)
group=[]
p=t[0][1]
group.append(t[0])
for i in range(1,n):
	if (t[i][0]>p):
		group.append(t[i])
		p=t[i][1]
print(group)

