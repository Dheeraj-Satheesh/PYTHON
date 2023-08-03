def sum_digit(number):
    total = 0
    count = 0
    temp = number
    while number:
        total += number%10
        number = number//10
        count += 1
    return temp,count,total 
n = int(input())
sum_list = []
for i in range(n):
    number = int(input())
    sum_list.append(sum_digit(number))
count = 0
for i in range(1,n):
    if sum_list[0][1] == sum_list[i][1] and sum_list[0][2] == sum_list[i][2]:
        if count == 0:
            print(sum_list[0][0])
        print(sum_list[i][0])
        count += 1
if count == 0:
    print('No sum-equivalent')