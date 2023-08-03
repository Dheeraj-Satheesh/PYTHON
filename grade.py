n=int(input())
l=[]
for i in range(n):
    name=input()
    reg=input()
    m1=int(input())
    m2=int(input())
    m3=int(input())
    m4=int(input())
    m5=int(input())
    sum=m1+m2+m3+m4+m5
    l.append([name,reg,(m1,m2,m3,m4,m5),sum])
print(l)   
