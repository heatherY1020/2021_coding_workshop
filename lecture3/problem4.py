s = 'a' + str(input())
l = []
for i in s:
	l.append(ord(i))
m = 0
for k in range(0,len(s)-1):
	b = l[k]-l[k+1]
	if 0<b<=13:
		b = b
	elif -13<=b<=0:
		b = -b
	elif 13<b:
		b = 26 - b
	else:
		b = 26 + b
	m +=b
print(m)