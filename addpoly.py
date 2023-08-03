num1 = int(input())
polynomial1 = []
for i in range(num1+1):
    polynomial1.insert(i,eval(input()))
num2 = int(input())
polynomial2 = []
for i in range(num2+1):
    polynomial2.insert(i,eval(input()))
if num1 < num2:
    for i in range(num2-num1):
        polynomial1.insert(0,0)
elif num1 > num2:
    for i in range(num1-num2):
        polynomial2.insert(0,0)
maxi = num1+1 if num1 >= num2 else num2+1
total = []
for i in range(maxi):
    total.insert(i,polynomial1[i]+polynomial2[i])
print(total)