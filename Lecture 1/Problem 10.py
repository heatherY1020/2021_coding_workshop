de = int(input())
bi = de%2 + de//2%2*10 + de//4%2*100 + de//8%2*1000

print(bi)