order=int(input())
if order>0:
    matrix=[]
    for i in range(0,order):
        matrix.append([])
        for j in range(0,order):
            n=int(input())
            matrix[i].append(n)          
    for i in range(0,order):
        for j in range(0,order):
            if matrix[i][j]!=matrix[j][i]:
                print("Not symmetric")
                exit()
    print("Symmetric")  
else:
    print("Invalid input")

