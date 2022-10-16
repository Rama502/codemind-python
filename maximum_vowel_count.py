x=list(map(str,input().split()))
n=[]
s=0
I=['a','e','i','o','u']
for i in x:
    for j in i:
        if j in I:
            s+=1
    n.append(s)
    s=0
print(max(n))