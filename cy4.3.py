a=int(input())
b=int(input())
L=[]
for i in range(a):
    l=list(input().spllit())
    L.append(l)
m=int(input())
n=int(input())
for i in L:
    if int(i[m])==n:
        print('[%s]'%(', '.join(i)))
        
     
    