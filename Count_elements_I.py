a,b=map(int,input().split())
I=list(map(int,input().split()))
m=list(map(int,input().split()))
k=[]
c=0
for i in range(a):
    if I[i] in m:
        k.append(I[i])
print(len(set(k)))a