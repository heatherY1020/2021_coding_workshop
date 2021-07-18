# 사탕 개수 입력, 규칙에 따른 분배의 경우 출력.

x = int(input())

for m in range(int(x/2), 0, -1):
    for n in range(x-m, 0, -1):
        k = x - m - n
        if m>n and m>k:
            output = m, n, k
            print(output)