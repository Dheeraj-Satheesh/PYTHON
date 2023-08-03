n=int(input())
ml=0
for i in range(n):
    l=int(input())
    m=int(input())
    ml=ml+m+l*1000
litre=ml//1000
ml=ml%1000
print(str(litre)+'litre'+str(ml)+' '+'ml')

