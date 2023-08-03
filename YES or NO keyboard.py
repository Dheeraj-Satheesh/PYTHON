word = input()
length = len(word)
c = True
row = 0
for i in range(length):
    if word[i] in 'qwertyuiopQWERTYUIOP':
        if row in [2,3]:
            c = False
            break
        row = 1
    elif word[i] in 'asdfghjklASDFGHJKL':
        if row in [1,3]:
            c = False
            break
        row = 2
    elif word[i] in 'zxcvbnmZXCVBNM':
        if row in [1,2]:
            c = False
            break
        row = 3
if c == True:
    print("Yes")
else:
    print("No")
