p=int(input())
def sum(x):
    n=0
    l=[]
    for i in range(x):
        l.append(int(input()))
        n+=int(l[i])
    return n
print(sum(p))
    