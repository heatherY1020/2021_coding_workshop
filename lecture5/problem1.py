a = list(map(int, input().split()))
b = list(map(int, input().split()))
b.sort()
output = 0
for i in b:
	output +=i*a[1]
	a[1] -=1
	if a[1] == 0:
		a[1] += 1
print (output)