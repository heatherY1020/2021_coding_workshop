#영단어 입력. 제시된 장치로 해당 단어를 얻기 위해 필요한 회전수 출력.

word = input()
sum = 0
table = 'abcdefghijklmnopqrstuvwxyz'

bias = 0
for step in word:
    num = abs(bias - table.find(step))
    bias = table.find(step)
    if num <= (26-num):
        sum += num
    else:
        sum += 26-num

print(sum)