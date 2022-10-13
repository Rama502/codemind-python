s=input()
p=s.split()
v='aeiouAEIOU'
c=0
d=[]
e=0
for i in p:
    c=0
    for j in i:
        if j in v:
            c=c+1
    d.append(c)
m=min(d)
for i in p:
    c=0
    for j in i:
        if j in v:
            c=c+1
    if c==m:
        e=e+1
print(e)