x1 = int(input())
y1 = int(input())
r1 = int(input())
x2 = int(input())
y2 = int(input())
r2 = int(input())
d1 = ((x1-x2)**2 + (y1-y2)**2)**(1/2)
d2 = r1 + r2
if r1 >= r2:
	d3= r1-r2
else:
	d3 = r2 - r1
if d1>0:
	if d1>d2:
		print(0)
	elif d1==d2:
		print(1)
	elif d3<d1<d2:
		print(2)
	elif d3== d1:
		print(1)
	elif 0<d1<d3:
		print(0)
else:
	if r1 == r2:
		print(-1)
	else:
		print(0)
