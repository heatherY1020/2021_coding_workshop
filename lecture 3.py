#problem1
print('input number')
a = int(input())
s = '*'
for x in range(1,a+1):
	print(x*s)
#problem2
print('input number')
a = int(input())
b = 1
answer = 0
L = []
while a >= 1:
        c = a%2
        d = a//2
        L.append(c)
        a=d
for x in range(len(L)-1,-1,-1):
        answer = answer*10+L[x]
print(answer)
#problem3
print('input a')
a = int(input())
print('input b')
b = int(input())
a_b = a+b
A = []
B = []
A_B = []
a_answer = 0
b_answer = 0
a_b_answer = 0
while a > 0:
	c = a%10
	A.append(c)
	a = int(a/10)
while b > 0:
	d = b%10
	B.append(d)
	b = int(b/10)
while a_b > 0:
	e = a_b%10
	A_B.append(e)
	a_b = int(a_b/10)
for x in range(len(A)-1,-1,-1):
	if A[x] == 0:
		A.pop(x)
	else:
		a_answer = a_answer*10+A[x]
for y in range(len(B)-1,-1,-1):
	if B[y] == 0:
		B.pop(y)
	else:
		b_answer = b_answer*10+B[y]	

for z in range(len(A_B)-1,-1,-1):
	if A_B[z] == 0:
		A_B.pop(z)
	else:
		a_b_answer = a_b_answer*10+A_B[z]
if a_answer+b_answer == a_b_answer:
	print('YES')
else:
	print('NO')
#problem4
rotation=0
L = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
print("input word")
A = input()
if L.index(A[0])>13:
	rotation = 26-L.index(A[0])
else:
	rotation = L.index(A[0])
for x in range(1,len(A)):
	if abs(L.index(A[x-1])-L.index(A[x]))>13:
		rotation = rotation + 26 - abs(L.index(A[x-1])-L.index(A[x]))
	else:
		rotation = rotation + abs(L.index(A[x-1])-L.index(A[x]))
print(rotation)
#problem5
print('input five numbers')
L=[]
for x in range(5):
	L.append(int(input()))
D=[]
for y in range(5):
	D.append(L[0]+L[1]+L[2]+L[3]+L[4]-L[y])
answer_max = D[0]
answer_min = D[0]
print(D)
for z in range(5):
	if answer_min>=D[z]:
		answer_min=D[z]
	if answer_max<=D[z]:
		answer_max=D[z]
		print(answer_max)
print(answer_min,answer_max)
#problem6a
print('input report')
A=input()
score='pass'
a = A.replace('\\n', ' ').replace('.', '').replace(',', '').replace('?', '').replace("'", '').replace('A', 'a').replace('B', 'b').replace('C', 'c').replace('D', 'd')
b = a.replace('E', 'e').replace('F', 'f').replace('G', 'g').replace('H', 'h').replace('I', 'i').replace('J', 'j').replace('K', 'k').replace('L', 'l').replace('M', 'm').replace('N', 'n').replace('O', 'o')
c = b.replace('P', 'p').replace('Q', 'q').replace('R', 'r').replace('S', 's').replace('T', 't').replace('U', 'u').replace('V', 'v').replace('W', 'w').replace('X', 'x').replace('Y', 'y').replace('Z', 'z')
e = c.split()
W_1 = e.count('the')
W_2 = e.count('a')
W_3 = e.count('an')
W_4 = e.count('for')
W_5 = e.count('and')
W_6 = e.count('nor')
W_7 = e.count('but')
W_8 = e.count('or')
W_9 = e.count('yet')
W_10 = e.count('because')
W_11 = e.count('although')
W_12 = e.count('since')
W_13 = e.count('unless')
W_14 = e.count('while')
W_15 = e.count('where')
W_16 = e.count('what!')
W_17 = e.count('ah!')
W_18 = e.count('oh!')
W_19 = e.count('shh!')
W = W_1 + W_2 + W_3 + W_4 + W_5 + W_6 + W_7 + W_8 + W_9 + W_10 + W_11 + W_12 + W_13 + W_14 + W_15 + W_16 + W_17 + W_18 + W_19
if W/len(e)>0.1:
        score='Fail'
f = c.replace(' ', '').replace('!', '')
if len(f)<5000:
        score='Fail'
if score=='Fail':
        print('See you next year')
else:
        print(score)
#problem6b
print('input report A')
A=input()
print('input report B')
B=input()
score='pass'
a = A.replace('\\n', ' ').replace('.', '').replace(',', '').replace('?', '').replace("'", '').replace('A', 'a').replace('B', 'b').replace('C', 'c').replace('D', 'd')
b = a.replace('E', 'e').replace('F', 'f').replace('G', 'g').replace('H', 'h').replace('I', 'i').replace('J', 'j').replace('K', 'k').replace('L', 'l').replace('M', 'm').replace('N', 'n').replace('O', 'o')
c = b.replace('P', 'p').replace('Q', 'q').replace('R', 'r').replace('S', 's').replace('T', 't').replace('U', 'u').replace('V', 'v').replace('W', 'w').replace('X', 'x').replace('Y', 'y').replace('Z', 'z')
k = c.split()
e = set(k)
if 'the' in e:
        e.remove('the')
if 'a' in e:
        e.remove('a')
if 'an' in e:
        e.remove('an')
if 'for' in e:
        e.remove('for')
if 'and' in e:
        e.remove('and')
if 'nor' in e:
        e.remove('nor')
if 'but' in e:
        e.remove('but')
if 'or' in e:
        e.remove('or')
if 'yet' in e:
        e.remove('yet')
if 'because' in e:
        e.remove('because')
if 'although' in e:
        e.remove('although')
if 'since' in e:
        e.remove('since')
if 'unless' in e:
        e.remove('unless')
if 'while' in e:
        e.remove('while')
if 'where' in e:
        e.remove('where')
if 'what!' in e:
        e.remove('what!')
if 'ah!' in e:
        e.remove('ah!')
if 'oh!' in e:
        e.remove('oh!')
if 'shh!' in e:
        e.remove('shh!')
print(e)
a_b = B.replace('\\n', ' ').replace('.', '').replace(',', '').replace('?', '').replace("'", '').replace('A', 'a').replace('B', 'b').replace('C', 'c').replace('D', 'd')
b_b = a_b.replace('E', 'e').replace('F', 'f').replace('G', 'g').replace('H', 'h').replace('I', 'i').replace('J', 'j').replace('K', 'k').replace('L', 'l').replace('M', 'm').replace('N', 'n').replace('O', 'o')
c_b = b_b.replace('P', 'p').replace('Q', 'q').replace('R', 'r').replace('S', 's').replace('T', 't').replace('U', 'u').replace('V', 'v').replace('W', 'w').replace('X', 'x').replace('Y', 'y').replace('Z', 'z')
k_b = c_b.split()
e_b = set(k_b)
if 'the' in e_b:
        e_b.remove('the')
if 'a' in e_b:
        e_b.remove('a')
if 'an' in e_b:
        e_b.remove('an')
if 'for' in e_b:
        e_b.remove('for')
if 'and' in e_b:
        e_b.remove('and')
if 'nor' in e_b:
        e_b.remove('nor')
if 'but' in e_b:
        e_b.remove('but')
if 'or' in e_b:
        e_b.remove('or')
if 'yet' in e_b:
        e_b.remove('yet')
if 'because' in e_b:
        e_b.remove('because')
if 'although' in e_b:
        e_b.remove('although')
if 'since' in e_b:
        e_b.remove('since')
if 'unless' in e_b:
        e_b.remove('unless')
if 'while' in e_b:
        e_b.remove('while')
if 'where' in e_b:
        e_b.remove('where')
if 'what!' in e_b:
        e_b.remove('what!')
if 'ah!' in e_b:
        e_b.remove('ah!')
if 'oh!' in e_b:
        e_b.remove('oh!')
if 'shh!' in e_b:
        e_b.remove('shh!')
print(set(e),set(e_b))
e_i = set(e).intersection(set(e_b))
print(e_i)
qq = len(e_i)/len(set(e))
print(qq)
W_1 = k.count('the')
W_2 = k.count('a')
W_3 = k.count('an')
W_4 = k.count('for')
W_5 = k.count('and')
W_6 = k.count('nor')
W_7 = k.count('but')
W_8 = k.count('or')
W_9 = k.count('yet')
W_10 = k.count('because')
W_11 = k.count('although')
W_12 = k.count('since')
W_13 = k.count('unless')
W_14 = k.count('while')
W_15 = k.count('where')
W_16 = k.count('what!')
W_17 = k.count('ah!')
W_18 = k.count('oh!')
W_19 = k.count('shh!')
W = W_1 + W_2 + W_3 + W_4 + W_5 + W_6 + W_7 + W_8 + W_9 + W_10 + W_11 + W_12 + W_13 + W_14 + W_15 + W_16 + W_17 + W_18 + W_19
if W/len(k)>0.1:
        score='Fail'
f = c.replace(' ', '').replace('!', '')
if len(f)<5000:
        score='Fail'
if qq>0.4:
        score='See you never again'
        print(score)
elif score=='Fail':
        print('See you next year')
else:
        print(score)
#problem7
print('input numbers')
A_o = input()
B_o = input()
C_o = input()
D_o = input()
E_o = input()
A = []
B = []
C = []
D = []
E = []
for x in range(5):
        A.append(A_o[x])
for x in range(5):
        B.append(B_o[x])
for x in range(5):
        C.append(C_o[x])
for x in range(5):
        D.append(D_o[x])
for x in range(5):
        E.append(E_o[x])
print(A,B,C,D,E)
A.count('1')
B.count('1')
C.count('1')
D.count('1')
E.count('1')