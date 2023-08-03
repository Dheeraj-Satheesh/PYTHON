a = float(input())  
b = float(input())  
c = float(input())  
s = (a + b + c) / 2  
Area = (s*(s-a)*(s-b)*(s-c)) ** 0.5  
print(' %0.2f' %Area)