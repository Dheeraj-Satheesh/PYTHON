import re
s = ' Rahul got 75 marks, Vijay got 55 marks, whereas Subbu got 98 marks.'
marks= re.findall(r'(?:^|(?<=[\W_]))[1234567890][^\W_]*(?=[\s_]|$)', s, re.I)
marks2=re.findall(r'(?<!^)(?<!\. )[A-Z][a-z]+',s)
print(marks)
print(marks2)
