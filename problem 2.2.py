age=int(input())
height=float(input())
weight=int(input())
chest=int(input())

if age<0 or height<0 or weight<0 or chest<0:
    print("Invalid input")
elif not 18<age<25:
    print("Disqualified due to age")
elif not 5.2<height<5.6:
    print("Disqualified due to height")
elif not 45<weight<60:
    print("Disqualified due to weight")
elif not chest<45:
    print("Disqualified due to chest")
else:
    print("Fit to army")
    

