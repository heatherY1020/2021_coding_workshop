number = int(input())
card_numbers = list(map(int, input().split(" ")))
sereja = 0
dima = 0

def ser():
    global sereja
    if card_numbers[0] > card_numbers[-1]:
        sereja += card_numbers[0]
        card_numbers.pop(0)
    else :
        sereja += card_numbers[-1]
        card_numbers.pop(-1)
        
def dim():
    global dima
    if card_numbers[0] > card_numbers[-1]:
        dima += card_numbers[0]
        card_numbers.pop(0)
    else :
        dima += card_numbers[-1]
        card_numbers.pop(-1)
        
def exit():
    if len(card_numbers) ==0:
        print(sereja, dima)
    else:
        pass
       
while len(card_numbers)>0:
    ser()
    exit()
    dim()
    exit()
