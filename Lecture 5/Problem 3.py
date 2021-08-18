a = input()
p = q = r = s = t = False

for i in a:
    if r == False:
        r = i.isdigit()
    if s == False:
        s = i.islower()
    if t == False:
        t = i.isupper()
    elif r and s and t == True:
        break

q = s or t
p = r or s or t

print(p, q, r, s, t, sep='\n')