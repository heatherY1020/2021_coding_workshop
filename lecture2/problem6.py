import math
x= int(input())
for m in range(math.ceil(x/3),int(x/2)+1):
	for n in range(0,x-m):
		k = x - m - n
		if m>n and m > k:
			output = (m, n, k)
			print(output)
