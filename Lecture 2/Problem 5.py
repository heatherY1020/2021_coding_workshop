# 두 원의 중심의 좌표와 반지름 입력, 두 원이 만나는 점의 개수 출력.
# 만약 만나는 점이 특정되지 못한다면, -1 출력.

x1 = int(input())
y1 = int(input())
r1 = int(input())
x2 = int(input())
y2 = int(input())
r2 = int(input())

squared_d = ((x1-x2)**2 + (y1-y2)**2)

if (x1==x2) and (y1==y2) and (r1==r2) and (r1!=0):
    output = -1
elif (squared_d<(r1+r2)**2) and (squared_d>(r1-r2)**2):
    output = 2
elif (squared_d==(r1+r2)**2) or (squared_d==(r1-r2)**2):
    output = 1
else:
    output = 0

print(output)