n=int(input())
sum=0
p=n*n
o=n
while p:
    r=p%10
    p=p//10
    sum+=r
if sum==o:
    print('Neon Number')
else:
    print('Not Neon Number')