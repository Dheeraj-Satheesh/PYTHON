l=int(input())
L=list(input().split())
l_s=0
r_s=0
x=0
for i in range(1,l-1):
    for j in range(0,i):
        l_s+=int(L[j])
    for k in range(i+1,l):
        r_s+=int(L[k])
    if l_s==r_s:
        print(i)
        x=1
    l_s=0
    r_s=0
if x==0:
    print(0)