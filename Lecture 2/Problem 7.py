# A, B, C를 입력, N*A+B < N*C를 만족하는 최소의 N 출력.
# 그러한 N이 없다면, False 출력.

a = int(input())
b = int(input())
c = int(input())

if a>=c:
    print(False)
else:
    n = 1
    while True:
        if (n*a+b)<(n*c):
            break
        else:
            n += 1
    print(n)