stud = int(input())
list = []
if stud > 0:
    for i in range(stud):
        a = int(input())
        if a >= 50:
            list.append(a)
        elif a <= 0:
            print('Invalid input')
    print(len(list))
else:
    print('Invalid input')    