n=int(input())
if n>1:
    if n%2==0:
        for i in range(2,n+1,2):
            fac=1
            for j in range(1, i+1):
                fac= fac*j
            print(i," ",fac)    
    else:
        for i in range(1,n+1,2):
            fac =1
            for j in range(1,i+1):
                fac= fac*j
            print(i, " ",fac)
else:
    print("Invalid input")
            
            
                

        

