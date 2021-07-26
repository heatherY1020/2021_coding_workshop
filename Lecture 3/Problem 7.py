#틱택토 하세요~

ttt = []
for i in range(5):
    ttt.append(list(input()))

result = []

for y in range(5):
    for x in range(2):
        sum = 0
        for alpha in range(4):
            if ttt[y][x+alpha] == '1':
                sum += 1
        if sum == 3:
            for alpha in range(4):
                if ttt[y][x+alpha] == '0':
                    result.append((y, x+alpha))

for x in range(5):
    for y in range(2):
        sum = 0
        for alpha in range(4):
            if ttt[y+alpha][x] == '1':
                sum += 1
        if sum == 3:
            for alpha in range(4):
                if ttt[y+alpha][x] == '0':
                    result.append((y+alpha, x))

for y in range(2):
    for x in range(2):
        sum = 0
        for alpha in range(4):
            if ttt[y+alpha][x+alpha] == '1':
                sum += 1
        if sum == 3:
            for alpha in range(4):
                if ttt[y+alpha][x+alpha] == '0':
                    result.append((y+alpha, x+alpha))
    for x in range(3, 5):
        sum = 0
        for alpha in range(4):
            if ttt[y+alpha][x-alpha] == '1':
                sum += 1
        if sum == 3:
            for alpha in range(4):
                if ttt[y+alpha][x-alpha] == '0':
                    result.append((y+alpha, x-alpha))

if len(result) == 0:
    print(None)
else:
    for prt in result:
        print(prt)