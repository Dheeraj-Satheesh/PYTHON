n=int(input())
i=float(input())
s=int(input())
if n>0 and i>0 and s>0:
    if n>=500 and i>=1 and s>=300:
        print("Platinum customer")
    elif n>=500 and i>=1:
        print("Golden customer")
    elif n>=500 and s>=300:
        print("Valuable customer")
else:
    print("Invalid input")
    
        

 