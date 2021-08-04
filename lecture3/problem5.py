k = list
k = a, b, c, d, e = list(map(int, input().split()))
t = k[:]
k.remove(max(k))
t.remove(min(t))
print(sum(k), sum(t))
