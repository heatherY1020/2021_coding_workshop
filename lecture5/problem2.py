a = list(map(int, input().split()))
b = list(map(int, input().split()))
b.sort()
print(b[a[2]]-b[a[2]-1])