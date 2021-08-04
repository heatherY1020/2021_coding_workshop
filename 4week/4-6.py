a = []
b = []
cnt = 0 
k = 0
c = []
d = []

# c++에서는 abcd를 int 배열로 썼는데 여기서는 리스트로 사용함
# 리스트 요소만 int로 맞춰주면 다를거 없더라

n, m, x, y = map(int, input("start >>\n").split())

a.extend(input().split())
a = list(map(int, a))
# print(a) - 리스트 요소 int 맞나 확인용으로 넣어놓은거

b.extend(input().split())
b = list(map(int, b))
# print(b) - 상동
	
a.sort()
b.sort()
# 오름차순 정렬

for i in range(0, n):
	while(a[i]-x > b[k] and k < m):
		k = k + 1
		# c에서 k++은 k=k+1인데 파이썬에는 이 연산자가 없어서 그냥 풀어씀
		
	if(a[i] + y < b[k]):
		continue
	if(k == m):
		break
	
	c.append(i+1)
	d.append(k+1)
	# c++에서는 비어있는 배열에 값을 집어넣는 거였는데
	# 리스트로 바꿨으니까 append 써줬음
	
	cnt = cnt +1
	k = k +1
	# 위 while의 k와 같은 이유

print("---result---")
print("{}" .format(cnt))

for i in range(0, cnt):
	print("{} {}" .format(c[i], d[i]))
