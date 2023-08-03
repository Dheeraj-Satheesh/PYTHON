def max(n1,n2,n3):
    if (n1>=n2) and (n1>=n3):
        return n1
    elif (n2>=n1) and (n2>=n3):
        return n2
    else:
         return n3
n1=int(input())
n2=int(input())
n3=int(input())
print(max(n1,n2,n3))   
   
