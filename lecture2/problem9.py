n, m, a = list(map(int, input().split()))
b = 1
while a*b<n:
	b += 1
c = 1
while a*c<m:
	c += 1
print (b*c)