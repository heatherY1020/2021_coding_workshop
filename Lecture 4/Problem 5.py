num = int(input())
deck = list(map(int, input().split()))

a, b = 0, 0

while(len(deck) > 0):
    if deck[0] > deck[-1]:
        a += deck[0]
        del deck[0]
    else:
        a += deck[-1]
        del deck[-1]
    if len(deck) > 0:
        if deck[0] > deck[-1]:
            b += deck[0]
            del deck[0]
        else:
            b += deck[-1]
            del deck[-1]
    else:
        break

print(a, b)