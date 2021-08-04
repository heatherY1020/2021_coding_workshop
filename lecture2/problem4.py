a = int(input())
while True:
	a+=1
	c = 0
	for i in range(2,a):
		if a%i==0:
			c=1
	if c ==0:
		break
print(a)


