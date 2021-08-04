a = float(input())
b = ''
if a%1==0:
	while a>0:
		b = str(int(a%2))+ b
		a=a//2
	print(b)
else:
	print(False)