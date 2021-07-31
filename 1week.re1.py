#1
print("Hello, World!!!")
#2
print("   ∧＿∧\nｒy´・ω・｀ヽっ \n `!       i \n ゝc＿c_,.ノ")

#3
#60을 0으로 나눌 수 없어서

#4
#string은 interger와 더할 수 없음

#5
print(type(123+123.0))
print(type(246.0+False+True))
print(type("123"+"None"))

#6
a=int(input("Math score :"))
b=int(input("Korean score :"))
c=int(input("Science score:"))
def mean(x,y,z) :
    return ((x+y+z)/3)
print(mean(a,b,c))

#7
A=int(input("first number?"))
B=int(input("second number?"))
print(A//B, A%B, sep='\n')

#8
x=int(input("first salary?"))
y=int(input("second salary?"))
z=int(input("third salary?"))
_x=int(input("fourth salary?"))
import numpy as 푸름
print(푸름.sum([x,y,z,])-_x)

#9
import time
fseconds=time.time()
#print(int(fseconds))

fday=fseconds/86400
if fday-int(fday) !=0:
    global f2day
    f2day = int(fday)+1
fmonth= int(1+((fday/30)%12))
if fmonth>12:
    fmonth-=12
fyear=1970+(fday/360)
if fyear-int(fyear) !=0:
    fyear = int(fyear)+1
r_fday=1+(f2day%30)
if r_fday>30:
    r_fday-=30
print("Today's Year: "+str(fyear))
print("Today's Month: "+str(fmonth))
print("Today's Day: "+str(r_fday))

#10
xx=int(input("number?"))
print("method1: ", bin(xx))
result=""
r_result=""
while xx>=1:
    if xx%2==1:
        result+= "1"
        xx=(xx-1)/2
    else:
        xx/=2
        result+= "0"
    if xx==1:
        result+= "1"
        break
for i in range(0,len(result)):
    r_result +=result[(-1*i)+len(result)-1]
print("method2: ",r_result)

#11
yy=input("5자리 숫자만 써라...")
def sigma():
    global result2
    result2 = 0
    for i in range(0,len(yy)):
        result2+= int(yy[i])
    print(result2)
sigma()


