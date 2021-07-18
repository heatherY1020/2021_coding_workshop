# 연도를 입력, 윤년 여부를 출력.

year = int(input())

if year%4==0:
    if year%100==0:
        if year%400==0:
            print(True)
        else:
            print(False)
    else:
        print(True)
else:
    print(False)