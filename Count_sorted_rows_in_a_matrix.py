def sor(l):
    m=sorted(l)
    n=sorted(l,reverse=True)
    if l==m or l==n:
        return l
a,b=map(int,input().split())
mat=[]
c=0
for i in range(a):
    x=list(map(int,input().split()))
    mat.append(x)
for i in range(a):
    z=[]
    for j in range(b):
        z.append(mat[i][j])
    if sor(z):
        c+=1
print(c)