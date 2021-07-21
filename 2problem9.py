n=6
m=6
a=4
if n==a:
    x=1
else:
    if n%a==0:
        x=n//a
    else:
        x=n//a+1
if m==a:
    y=1
else:
    if m%a==0:
        y=m//a
    else:
        y=m//a+1
print(x*y)