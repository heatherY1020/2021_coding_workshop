a= int(input())
b= int(input())
c = int(input())
if a >= c:
	print(False)
else:
	i = 1
	while i <= b/(c-a):
		i = i + 1
	
	print(i)

