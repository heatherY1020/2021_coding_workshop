# 5개의 숫자 입력, 순서대로 커진다면 YES, 아니라면 NO 출력.
# 0이 입력되면 프로그램 종료.

a = int(input())
if a==0: exit()
b = int(input())
if b==0: exit()
c = int(input())
if c==0: exit()
d = int(input())
if d==0: exit()
e = int(input())
if e==0: exit()

if (a<b) and (b<c) and (c<d) and (d<e):
    print('YES')
else:
    print('NO')