"""mark >=90 S
90>mark >=80 A
80>mark >=70 B
70>mark >=60 C
60>mark >=55 D
55>mark >=50 E"""
  


mark=float(input())
if mark>=90:
    print("S")
elif mark>=80 and mark<90:
    print("A")
    mark>=70 and mark<80
    print("B")
    mark>=60 and mark<70
    print("C")
    mark>=55 and mark<60
    print("D")
    mark>=50 and mark<55
    print("E")
else:
     print("F")         
   
          
       
    