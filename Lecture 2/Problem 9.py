# 직사각형의 가로와 세로 그리고 정사각형 타일의 길이 입력.
# 직사각형을 덮기 위해 필요한 최소의 타일 개수 출력.

n, m, a = list(map(int, input().split()))

w = n//a + 1
h = m//a + 1

print(w*h)