hrs=int(input())
if 7<hrs<=8:
    print(200)
elif 8<hrs<13:
    print(200+((hrs-8)*100))
elif 12<hrs<17:
    print(600+((hrs-12)*200))
elif hrs>16:
    print(1400+((hrs-16)*250))
else:
    print("Invalid input")
    
          
    
    