m=float(input())
if m>0:
    c=input("")
    if m>=80 and c=="T":
            print(m+m*0.08)
    elif m>=80 and c=="L":
            print(m+m*0.06)
    elif 80>m>=60 and c=="T":
            print(m+m*0.06)
    elif 80>m>=60 and c=="L":
            print(m+m*0.04)
    elif 60>m>=40 and c=="T":
            print(m+m*0.04) 
    elif 60>m>=40 and c=="L":
           print(m+m*0.02)
    elif 40>m>=1 and c=="T":
            print(m)
    elif 40>m>=1  and c=="L":
            print(m)
else:
    print("Enter the appropriate mark")
        

    
