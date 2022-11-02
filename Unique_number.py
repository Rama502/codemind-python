b=input()
c=[]
for i in b:
    c.append(i)
#print(c)
for i in c:
    if ((c.count(i))>1):
        print("Not Unique Number")
        break
else:
    print("Unique Number")