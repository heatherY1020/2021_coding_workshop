limit =int(input())

def frm(x):
    i = str(x)
    if len(i) ==0:
        print("check the number again")
    elif len(i) ==2 or len(i) ==3:
        if i[0] ==i[-1]:
            print(i)
    elif len(i) ==1:
        print(i)
           
while limit>0:
    frm(limit)
    limit-=1

    if limit ==0:
        break
    
    
