#1
a = int(input("number"))
for i in range (1,a+1):
    b = -i+a
    print(" "*b+"*"*i)

#2
xx=int(input("number?"))
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
if xx == 0:
    r_result = 0
print("binary_result : ", r_result)

#3
A = input()
B = input()
a = ""
b=""
pred_c=""
pred_C = int(A)+int(B)
pred_C = str(pred_C)
for i in A:
    if i!="0":
      a+=i
for j in B:
    if j!="0":
        b+=j
for k in pred_C:
    if k !="0":
        pred_c +=k
c = int(a)+int(b)
if int(pred_c) ==c:
    print("YES")
else:
    print("NO")

#4
alp = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
name = input()
number = []
for i in name:
    for idj, j in enumerate(alp):
        if i == j:
            number.append(int(idj))
def distance(x):
    n1 = min(number[x], number[x+1])
    n2 = max(number[x], number[x+1])
    d1 = n2-n1
    d2 = (25-n2)+(n1+1)
    return min(d1, d2)
sum = min((26-number[0]), number[0])
for j in range(len(name)-1):
    sum +=distance(j)
print(sum)

#5
arr = list(map(int, input().rstrip().split()))
def miniMaxSum(arr):
    n5 = max(arr)
    n1 = min(arr)
    plus = sum(arr)
    mini = plus-n5
    maxi = plus-n1
    print(mini, maxi)
miniMaxSum(arr)

#6
