n=int(input())
s=0
if n>0:
     for i in range(1,2*n,2):
         s+=i
     print(s)
else:
    print("Invalid input")

