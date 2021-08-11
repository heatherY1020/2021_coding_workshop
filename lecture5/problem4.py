n = int(input())
a = list(map(int, input().split()))
ar = sorted(a)
result = 0
for i in range(n+1):
	for p in range(i):
		k = list(reversed(a[p:i]))
		if a[0:p] + k + a[i:n] == ar:
			result = 'yes'
			break
		else:
			result = 'no'
print(result)