n, m, x, y = map(int, input().split(" "))
a = list(map(int, input().split(" ")))
b = list(map(int, input().split(" ")))

A = a.sort()
B = b.sort()

for i in range (n) :
    while (a[i]-x >b[k]) and (k<m):
        if a[i]+y <b[k]:
            continue
        if k==m:
            break
        
           
for i in range(n):
    for j in range(m):
        
