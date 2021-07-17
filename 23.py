#problem 1
print("input year")
a=int(input())
b=a%4
c=a%100
d=a%400
if b==0:
	if c==0:
		if d==0:
			print("True")
		else: 
			print("False")
	else :
		print("True")				
else:
	print("False")
#problem 2
print("input hour")
a=int(input())
print("input minute")
b=int(input())
if a==0:
	if b<45:
		a=11
		b=b+15
	else:
		b=b-45
else:
	if b<45:
		a=a-1
		b=b+15
	else:
		b=b-45
print(a,b)
#problem 3
def prime_number(number):
    if number != 1:
        for f in range(2,number):
            if number % f == 0:
                return False
    else:
        return False
    return True
print("input number")
a = int(input())
max = 0

for i in range(a-1):
    if prime_number(i+1):
        max=i+1
if a==2 or a==1:
        print("False")
else:
        print('biggest prime number which is smaller than n is',max)
#problem 4

print("input number")
a = int(input())
min = a+1

while True:
        if prime_number(min):
                print('smallest prime number which is bigger than n is',min)
                break
        else:
                min+=1
#problem 5
import math
print("input theif1's location")
x_1=int(input())
y_1=int(input())
r_1=int(input())
print("input theif2's location")
x_2=int(input())
y_2=int(input())
r_2=int(input())
x=abs(x_1-x_2)
y=abs(y_1-y_2)
r=r_1+r_2
r_s=abs(r_1-r_2)
distance_square=x**2+y**2
if r<math.sqrt(distance_square):
        print(0)
elif r==math.sqrt(distance_square) or r_s==math.sqrt(distance_square):
        print(1)
elif x_1==x_2 and y_1==y_2 and r_1==r_2:
        print(-1)
elif math.sqrt(distance_square)<r and r_s<math.sqrt(distance_square):
        print(2)
else:
        print(0)
#problem6
print("input number")
a=int(input())
b=int(a/2)
for x in range(1,b+1):
        for y in range(1,a-x):
                if y>=x or a-x-y>=x:
                        continue
                else:
                        print(x,y,a-x-y)
#problem7
print("input A")
A=int(input())
print("input B")
B=int(input())
print("input C")
C=int(input())
n=0
if A>=C:
        print("False")
else:
        while n*A+B>=n*C:
                n=n+1
        print(n)
#problem8
print("input height of five trees")
a=int(input())
b=int(input())
c=int(input())
d=int(input())
e=int(input())
if a<b and b<c and c<d and d<e:
        print("YES")
else:
        print("NO")
#problem9
print("input n")
n=int(input())
print("input m")
m=int(input())
print("input a")
a=int(input())
x=1
y=1
while x*a<n:
        x=x+1
while y*a<m:
        y=y+1
print(x*y)

        
