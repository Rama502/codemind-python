n=int(input())
a=list(map(int,input().split()))
p=int(input())
for i in range(len(a)):
    if(a[i]==p):
        print(i)
        break
else:
    print("-1")
        
    