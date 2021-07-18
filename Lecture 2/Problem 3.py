# 자연수를 입력, 그보다 작은 최대의 소수를 출력.
# 없다면 False 출력.

def judgePrimeOdd(x):
    judgement = True
    int_sqrt_x = int(x ** 0.5)
    for k in range(3, int_sqrt_x + 1, 2):
        if x%k == 0:
            judgement = False
            break
    return judgement

n = int(input())

if n<=2:
    print(False)
elif n==3:
    print(2)
else:
    if n%2==0:
        for i in range(n-1, 1, -2):
            if judgePrimeOdd(i):
                p = i
                break
    else:
        for i in range(n-2, 1, -2):
            if judgePrimeOdd(i):
                p = i
                break
    print(p)