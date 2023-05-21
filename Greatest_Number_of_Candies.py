n=int(input())
a=list(map(int,input().split()))
p=int(input())
ma=0
for i in range(len(a)):
    if(ma<a[i]):
        ma=a[i]
for i in range(len(a)):
    q=a[i]+p
    if(q>=ma):
        print("True",end=" ")
    else:
        print("False",end=" ")

    
        
    