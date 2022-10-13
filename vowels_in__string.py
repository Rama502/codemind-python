n=input()
c=0
b=[]
for i in n:
    if i in 'aeiouAEIOU':
        c=c+1
        if i not in b:
            print(i,end=' ')
            b.append(i)
if c==0:
    print('-1')