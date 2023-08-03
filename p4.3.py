n = int(input())
a = []
b = []
c = []
for i in range(7):
    a.append([])
    b.append([])
    for j in range(n):
        a[i].append(int(input()))
        b[i].append(int(input()))

def srt(a, b):
    for j in range(n):
        t = 0
        for i in range(7):
            t += b[i][j]
        c.append([str(a[1][j]), float(f"{(t/7):.2f}")])
    c.sort(key = lambda x: x[1], reverse=True)
    return c
print(srt(a,b))