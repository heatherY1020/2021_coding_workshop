a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
if a==0 or b==0 or c==0 or d==0 or e==0:
	quit()
	
else:
	if a<b<c<d<e:
		print('YES')
	else:
		print('NO')