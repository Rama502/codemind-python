n=int(input())
a=list(map(int,input().split()))
sum1=0
sum2=0
for i in a:
    if i%2==0:
        sum1+=i
for i in a:
    if i%2!=0:
        sum2+=i  
diff=sum2-sum1
print(abs(diff))
    
    