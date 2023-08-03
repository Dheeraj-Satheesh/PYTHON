income=float(input())
if income <= 500000:
    tax=0
elif 500000<income<=1000000:
    tax=income*0.02
else:
    tax=income*0.04
print(tax)    