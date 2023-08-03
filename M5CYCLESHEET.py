A=[]
B=[]
C={}
a,b=0,0
n=int(input())
for i in range(n):
    Dict={}
    m=int(input())
    for j in range(m):
        key=str(input())
        value=int(input())
        Dict[key]=value
        if key not in B:
            B.append(key)
        B.sort()
    A.append(Dict)
for k in B:
    for i in A:
        for keys,values in i.items():
            if keys==k and values<50:
                a+=1
                break
    C[k]=a
    if a>0:
        b+=1
    a=0    
for keys,values in C.items():
    print(keys,values,sep='\n')
print(b)    
                    
            
    
    