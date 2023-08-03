word = input('')
word = word.lower()
length = len(word)
count=0
for i in range(0,length):
    for j in range(0,length):
        if word[i]==word[j]:
            count+=1
if count==len(word):
    print('GOOD')
else:
    print('BAD')
