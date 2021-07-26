#십진수 양수 입력. 이진수 출력. 먄약 입력이 정수가 아니라면 False 출력.

k = input()

if '.' in k:
    print(False)
else:
    q = [int(k)]
    r = ''
    counter = 0
    while True:
        if q[counter]<2:
            r += str(q[counter])
            break
        else:
            r += str(q[counter]%2)
            q.append(q[counter]//2)
            counter += 1
    r = int(r[::-1])
    print(r)