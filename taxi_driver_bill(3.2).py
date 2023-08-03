d=int(input())
if d<=10:
    bill=d*15
elif d<=100:
    bill=(d-10)*8+150
else:
    bill=870+(d-100)*6
print(bill)
       