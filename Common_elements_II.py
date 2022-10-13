a,b=map(int,input().split())
I1=list(map(int,input().split()))
I2=list(map(int,input().split()))
d=[]
c=0
for i in I1:
    if i not in I2:
        print(i,end=" ")
for i in I2:
    if i not in I1:
        print(i,end=" ")