PAN=input()
a=PAN[0:4].isupper()
b=PAN[5:8].isdigit()
c=PAN[-1].isupper()
if a==True and b==True and c==True:
    print("Valid")
else:
    print("invalid")
    
