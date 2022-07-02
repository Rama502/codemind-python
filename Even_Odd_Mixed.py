n=int(input())
s=0
even=0
odd=0
while(n>0):
    r=n%10
    s=s+1
    if(r%2==0):
        even+=1
    else:
        odd+=1
    n=n//10
if(odd>0 and even==0):
    print("Odd")
elif(even>0 and odd==0):
    print("Even")
else:
    print("Mixed")