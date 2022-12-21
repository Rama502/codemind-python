n=int(input())
for i in range(n):
    a=int(input())
    i=0
    r=0
    while a>0:#1011
        rema=a%10#3
        r=r+rema*(2**i)#
        a=a//10#1
        i+=1
    print(r)