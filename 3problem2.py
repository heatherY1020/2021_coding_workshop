num=input()
aList=[]
if type(num) ==int:   
    while num !=0:
        aList.append(num%2)
        num=num//2

    aList.reverse()

    print(aList)
else:
    print(False)