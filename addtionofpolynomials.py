n1 = int(input())
p1 = []
for i in range(0,n1+1):
    p1.append(int(input()))
n2 = int(input())
p2 = []
for i in range(0,n2+1):
    p2.append(int(input()))
if n1>n2:
    for i in range(-1,-(n2+2),-1):
        p1[i]=p1[i]+p2[i]
    print(p1)
else:
    for i in range(-1,-(n1+2),-1):
        p2[i]=p1[i]+p2[i]
    print(p2)    
        

    
     