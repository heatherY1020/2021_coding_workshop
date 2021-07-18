# 시간을 입력(24시간), 45분 전의 시간을 출력.

h = int(input())
m = int(input())

if m < 45:
    h -= 1
    m = 60 - (45 - m)
    if h == -1:
        h = 23
else:
    m -= 45

print(h)
print(m)