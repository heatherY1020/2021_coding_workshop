# 자연수를 입력, 그보다 큰 최소의 소수를 출력.

def judgePrimeOdd(x):
    judgement = True
    int_sqrt_x = int(x ** 0.5)
    for k in range(3, int_sqrt_x + 1, 2):
        if x%k == 0:
            judgement = False
            break
    return judgement

n = int(input())

if n==1:
    print(2)
else:
    if n%2==0:
        n += 1
    else:
        n += 2
    while True:
        if judgePrimeOdd(n):
            p = n
            break
        n += 2
    print(p)