import os
f=open("C:\\Users\\HP\\Downloads\\sender.dat","rb+")
statinfo=os.stat("C:\\Users\\HP\\Downloads\\sender.dat")
size=statinfo.st_size
n=int(input())
fp=n-1
while fp<size:
    f.seek(fp,0)
    ch=f.read(1)
    
    if ch ==b'1':
        
        f.seek(-1,1)
        f.write(b'0')
    else:
        
        f.seek(-1,1)
        f.write(b'1')
    fp+=n
f.seek(0,0)
print(f.read())
f.close    
    
        
        
        