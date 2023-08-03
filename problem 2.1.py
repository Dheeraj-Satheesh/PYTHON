days=int(input())
kms=int(input())
cost1=days*4000
cost2=days*1500+kms*9
if days>0 and kms>0:
    if cost1<cost2:
        print("Plan 1")
    else:
        print("Plan 2")
else:
    print("Invalid input")
        

