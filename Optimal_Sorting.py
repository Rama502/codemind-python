import math
z=int(input())
for i in range(z):
    n=int(input())
    a=list(map(int,input().split()))
    b=a
    s=sorted(a)
    q=len(s)
    if s==b:
        print('0')
    else:
        for i in range(q):
            t=s[q-1]-s[0]
        print(t)