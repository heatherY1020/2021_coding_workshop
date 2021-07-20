# 5개의 숫자 입력, 순서대로 커진다면 YES, 아니라면 NO 출력.
# 0이 입력되면 프로그램 종료.

counter = 0
t = []

while True:
    k = int(input())
    if k==0:
        exit()
    else:
        t.append(k)
        counter += 1
        if counter == 5:
            break


if (t[0]<t[1]) and (t[1]<t[2]) and (t[2]<t[3]) and (t[3]<t[4]):
    print('YES')
else:
    print('NO')