a = int(input())
b = int(input())
c = a + b
a = str(a)
b = str(b)
c = str(c)
a1 = int(a.replace('0',''))
b1 = int(b.replace('0',''))
c1 = int(c.replace('0',''))
if a1 + b1 == c1:
	print('YES')
else:
	print('NO')