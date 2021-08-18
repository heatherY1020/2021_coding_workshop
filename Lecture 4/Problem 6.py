n, m, x, y = map(int, input().split())
a = tuple(map(int, input().split()))
b = tuple(map(int, input().split()))

output = []

k, alpha = 0, 0

for vest in range(m):
    for guy in range(alpha, n):
        if a[guy]-x <= b[vest] <= a[guy]+y:
            output.append([guy+1, vest+1])
            k += 1
            alpha = guy+1
            break
        elif b[vest] < a[guy]-x:
            break

print(k)
for i in range(k):
    print(output[i][0], output[i][1])