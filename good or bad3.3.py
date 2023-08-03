s=input().lower()
length = len(s)
count=0
for i in range(0,length):
    for j in range(0,length):
        if s[i]==s[j]:
            count+=1
if count==len(s):
    print('Good')
else:
    print('Bad')