n=int(input())
s=0
while n>0 or s>=10:
    if n==0:
        n=s
        s=0
    s+=n%10
    n//=10
print(s)    
    