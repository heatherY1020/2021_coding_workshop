a = int(input())
if a <= 2:
	print('False')
else:
	for i in range(a-1,1,-1):
		c=0
		for j in range(2,i):
			if i%j ==0:
				c=1
		if c==0:
			break
	print(i)