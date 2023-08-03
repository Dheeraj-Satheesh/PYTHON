n=int(input())
a=[]
b=None
c=0
for i in range(n):
    m=int(input())
    for j in range(m):
        p=str(input())
        if j==0:
            b=p
        else:
            try:
                c+=int(p)
            except ValueError:
                continue
    q=(b,c)
    c=0
    a.append(q)
print(tuple(a))
    
            
               
                
            
      