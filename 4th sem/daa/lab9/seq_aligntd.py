def alignment(x,y,nx,ny,m):
	if nx==0:
		m[0][ny]=ny

	elif ny==0:
		m[nx][0]=nx

	elif x[nx-1] == y[ny-1]:
		m[nx][ny]=alignment(x,y,nx-1,ny-1,m)

	else:
		m[nx][ny]=min(1+alignment(x,y,nx-1,ny,m),1+alignment(x,y,nx,ny-1,m),1+alignment(x,y,nx-1,ny-1,m))

	return m[nx][ny]

def main():
	x="types"
	y="style"
	nx=len(x)
	ny=len(y)
	m=[[0 for i in range(nx+1)]for j in range(ny+1)]
	for i in range(nx+1):
		for j in range(ny+1):
			if i==0:
				m[0][j]=j
			if j==0:
				m[i][0]=i
	ans=alignment(x,y,nx,ny,m)
	for i in range(nx+1):
		for j in range(ny+1):
			print(m[i][j],end=' ')
		print()

	print("The answer is:",ans)

main()