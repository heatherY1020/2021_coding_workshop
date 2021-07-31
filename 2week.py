#2nd week assignment
#1
a = int(input("year?"))
if a%4==0:
    if a%100 ==0:
        if a%400 ==0:
             print("True")
        else:
            print("False")
    if a%100 !=0:
        print("True")
else:
    print("False")

#2
H = int(input("H :"))
if H<0 or H>23 :
    print("다시 입력해 주세요")
    H = int(input("H :"))
M = int(input("M :"))
if M<0 or M>59 :
    print("다시 입력해 주세요")
    M = int(input("M :"))

def getout():
 print("hour:{}".format(H), "min:{}".format(M), sep = '\n')

if M>=45:
    M -=45
    getout()
else:
    M +=15
    H -=1
    getout()
    
#3
#가장 큰 소수 구하기
n = int(input("number?"))
i = n-1
j = n-2
푸름 = []
def frm():
    global i, j
    while j>1:
        if i%j ==0:
            j -=1
            break
        else:
            j -=1
        if j ==1:
            #print(i, "소수임")
            푸름.append(i)
            break
if n>2:
    while i>1:
        frm()
        i -= 1
        j = i-1
        if i ==1:
            #print("소수 없음")
            break
    푸름.insert(len(푸름),2)
if n ==2:
    푸름.insert(len(푸름),2)
if n==1:
    pass
#print(len(푸름))
print("biggest prime number : ", 푸름[0])

#4
m = int(input("number :"))
ii = m+1
jj = 2
score = 0
def prime():
    global ii, jj, score
    while jj<ii:
        if ii%jj ==0:
            break
        else :
            jj +=1
        if jj == ii:
            score +=1
while True:
    prime()
    if score ==1:
        print("smallest prime number : ", ii)
        break
    else :
        ii +=1
        
#5
import math
xcor1 = float(input("x1 :"))
ycor1 = float(input("y1 :"))
xcor2 = float(input("x2 :"))
ycor2 = float(input("y2 :"))

dist1 = int(input("r1 :"))
while True :
    if dist1<0:
        print("distance should be larger than 0")
        dist1 = int(input("r1 :"))
    else :
        break
    
dist2 = int(input("r2 :"))
while True :
    if dist2<0:
        print("distance should be larger than 0")
        dist2 = int(input("r2 :"))
    else :
        break

distance = math.sqrt((xcor1-xcor2)**2+(ycor1-ycor2)**2)
subtract = max(dist1, dist2) - min(dist1, dist2)

if dist1==dist2 :
    if distance > (dist1+dist2):
        print('-1')
    if distance == (dist1+dist2):
        print('1')
    if distance == 0:
        print('-1')
    else :
        print("2")
if dist1 !=dist2:
    if distance > (dist1+dist2):
        print('-1')
    if distance == (dist1+dist2):
        print('1')
    if distance <(dist1+dist2) and distance> subtract:
        print('2')
    if distance == subtract :
        print('1')
    if distance< subtract:
        print('-1')

#6 
cn = int(input("candy number : "))
k = int(cn/2)
jjj = 1
while k>=(cn/3):
    if k<(cn/3):
        break
    while jjj<k:
        if jjj>=k:
            break
        elif (cn-k-jjj)<k:
                print("(", k, cn-k-jjj, jjj, ")")
                jjj +=1
        else:
          jjj +=1
    k-=1
    jjj=1

#7
import numpy as np
A=B=C= 0
while True:
    A= int(input("Variable Cost: "))
    B= int(input("Fixed Cost: "))
    C= int(input("Income per patient: "))
    if A>0 and B>0 and C>0:
        break
    else:
        print("음수가 있으므로 다시 입력해 주세요.")
        continue
if C<=A :
    print("False")
else:
    print(int(np.ceil(B/(C-A))))

#8
T1 = T2 = T3 = T4 = T5 = 0
score = 0
while True:
    T1= int(input("First Tree: "))
    T2= int(input("Second Tree: "))
    T3= int(input("Third Tree: "))
    T4= int(input("Fourth Tree: "))
    T5= int(input("Fifth Tree: "))
    if T1>0 and T2>0 and T3>0 and T4>0 and T5>0:
        break
    else:
        print("음수가 있으므로 다시 입력해 주세요.")
        continue
frm = [T1, T2, T3, T4, T5]
for i in range (len(frm)-1):
    if frm[i]>=frm[i+1]:
        score +=1
    else:
      pass

if score ==0:
  print("YES")
else :
  print("NO")


#9
from numpy import ceil
n, m, a = map(int, input().split())
xx = ceil(n/a)*ceil(m/a)
print(xx)
        
