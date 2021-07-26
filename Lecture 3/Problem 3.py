#양의정수 a, b 입력. a+b=c에서 0을 제거해도 참이라면 YES, 거짓이라면 NO 출력.

a = input()
b = input()
c = str(int(a)+int(b))

new_a = int(a.replace('0', ''))
new_b = int(b.replace('0', ''))
new_c = int(c.replace('0', ''))

if new_a + new_b == new_c:
    print('YES')
else:
    print('NO')