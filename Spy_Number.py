n=int(input())
sum=0
p=1
while n:
    r=n%10
    n=n//10
    sum+=r
    p*=r
if sum==p:
    print('Spy Number')
else:
    print('Not Spy Number')