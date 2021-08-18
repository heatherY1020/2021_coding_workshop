n, x = map(int, input().split())
cs = sorted(list(map(int, input().split())))

time = 0
for i in range(n):
    if x-i > 1:
        time += (x-i)*cs[i]
    else:
        time += cs[i]

print(time)