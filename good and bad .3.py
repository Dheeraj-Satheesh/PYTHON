s=input().lower()
cnt=0
for ltr in s:
    for itr in s:
        if itr==ltr:
            cnt=cnt+1
    if cnt>1:
        break
    cnt=0
if cnt==0:
    print("Good")
else:
    print("Bad")