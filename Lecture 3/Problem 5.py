#5개의 양의 정수 입력. 4개의 합의 최소와 최대 출력.

arr = list(map(int, input().split()))
sum_s = []

sum = 0
for num in arr:
    sum += num

for num in arr:
    sum_s.append(sum-num)

print(min(sum_s), max(sum_s))