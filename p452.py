import sys
def func_Read():
    fp=open('C:\\Users\\HP\Downloads\\ffcs.csv','r')
    print(fp.read())
    fp.close()
    
def func_Append(c):
    fp=open('C:\\Users\\HP\\Downloads\\ffcs.csv','a')
    fp.write('c')
    fp.close()
    
def func_Chk_Write(c):
    fp=open('C:\\Users\\HP\\Downloads\\ffcs.csv','r+')
    new_Line=c.split(',')
    line=fp.readline()
    already=False
    while line!='':
        fields=line.split(',')
        if new_Line[0]== fields[0]:
            already=True
        line=fp.readline()
    if not already:
        fp.write(c)
    fp.close()

def get_Details():
    reg_Num=input()
    name=input()
    age=input()
    gender=input()
    state=input()
    mobile=input()
    hobby=input()
    blood=input()
    details=reg_Num+','+name+','+age+','+gender+','+state+','+mobile+','+hobby+','+blood+','+'\n'
    return details
language_Spoken={'Malayalam':'Kerala','Tamil':'Tamilnadu'}

def find_Malayalee_Football():
    language1= 'Malayalam'
    malayalee_Football = 0
    state1=language_Spoken[language1]
    game1='Football'
    fp=open('C:\\Users\\HP\\Downloads\\ffcs.csv','r')
    line=fp.readline()
    while line!='':
        fields=line.split(',')
        if fields[3].strip()=='M' and\
           fields[4].strip()==state1 and\
           fields[6].strip()==game1:
               malayalee_Football+=1
        line=fp.readline() 
    fp.close()
    return malayalee_Football    

def find_Tamil_Agroup():
    blood='A+'
    language2='Tamil'
    state2=language_Spoken[language2]
    fp=open('C:\\Users\\HP\\Downloads\\ffcs.csv','r')
    line=fp.readline()
    while line!='':
        fields=line.split(',')
        if fields[3].strip()=='F' and\
           fields[4].strip()==state2 and\
           fields[7].strip()=='A+':
               print(fields[1],'\t',fields[5])
        line=fp.readline()
    fp.close()

func_Read()
s= get_Details()
func_Append(s)
func_Chk_Write(s)
func_Read()
count=find_Malayalee_Football()
print(count)
find_Tamil_Agroup()
               
        
           
            
    
    
    
    
    
    
    
    