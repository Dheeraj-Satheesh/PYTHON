n={}
a=[]
for i in range(4):
    m=int(input())
    a.append(m)
    l=[]
    for j in range(2,m+1):
        if(m%j==0):
            l.append(j)
    n[m]=l
p=set(n[a[0]])
q=set(n[a[1]])     
r=set(n[a[2]])
s=set(n[a[3]])        
k=p & q & r & s
common=list(k)
common.sort()
print(common)
i12=p & q
i34=r & s
second=list(i34-i12)
second.sort()
print(second)
