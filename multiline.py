#para=["23,24,25,26,27,34"]
#print(','.join(para))
para=[]
print("Enter a para : ")
while True:
        line=input()
        if line:
            para.append(line)
        else:
            break
print(para)
output='\n'.join(para)
print(output)