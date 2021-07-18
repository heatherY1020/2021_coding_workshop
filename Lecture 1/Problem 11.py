n = int(input())

a = n//10000
b = n//1000 - 10*a
c = n//100 - 100*a - 10*b
d = n//10 - 1000*a - 100*b - 10*c
e = n%10

print(a+b+c+d+e)