def edit(x,y):
    nx=len(x)
    ny=len(y)
    m=[[0 for i in range(ny+1)] for j in range(nx+1)]
    for i in range(nx+1):
        for j in range(ny+1):
            if i==0:
                m[0][j]=j
            if j==0:
                m[i][0]=i
    for i in range(1,nx+1):
        for j in range(1,ny+1):
            if x[i-1]==y[j-1]:
                d=0
            elif x[i-1]!=y[j-1]:
                d=1
            ans=min(1+m[i-1][j],1+m[i][j-1],d+m[i-1][j-1])
            m[i][j]=ans

    for i in range(nx+1):
        for j in range(ny+1):
            print(m[i][j]," ",end='')
        print()
    print()
    return m[nx][ny]

def main():
    x="types"
    y="style"
    ans=edit(x,y)
    print("the ans is: ",ans)

if __name__=='__main__':
    main()
  