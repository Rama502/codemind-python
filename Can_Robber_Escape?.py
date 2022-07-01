z=int(input())
arr=list(map(int,input().split()))
c=0
for i in range(z):
    if(arr[i]>=z):
        c=c+1
if c>0:
    print('NO')
else:
    print("YES")