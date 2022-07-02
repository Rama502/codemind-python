t=int(input())
for i in range(t):
    D,d,p,Q=map(int,input().split())
    n=D//d
    q=D%d
    s=0
    for i in range(n):
        s+=(p+(Q)*i)*d
    s+=(p+Q*n)*q
    print(s)