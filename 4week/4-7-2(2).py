# 대각선 탐색 함수(7B용)
def status_dictionary_diagonal(r, c, grid, result, mode):
    dia_to_row = ""
    row = r
    col = c
    while (row >= 0 and row <= 4 and col >= 0 and col <= 4):
        dia_to_row += grid[row][col]
        row += 1
        if mode == "left_down":
            col -= 1
        elif mode == "right_down":
            col += 1
    count = 0
    for i in range(len(dia_to_row)):
        if dia_to_row[i] == '2':
            count += 1
        else:
            if count == 2 or count == 3:
                result[count] += 1
                '''
                if mode == "left_down":
                    if grid[row - count - 1][col + count + 1] == '0' and grid[row][col] == '0':
                        result_grid[count].add((row - count - 1, col + count + 1))
                        result_grid[count].add((row, col))
                    if grid[row - count - 1][col + count + 1] == '1' and grid[row][col] == '0' and row - count <= 1 and col + count >= 1:
                        result_grid[count].add((row, col))
                    if grid[row - count - 1][col + count + 1] == '0' and grid[row][col] == '1' and col - 1 >= 3:
                        result_grid[count].add((row - count - 1, col + count + 1))
                elif mode == "right_down":
                    ''' # c 만들려다가 던짐 - 주석부분은 무시하기
            count = 0
    if count == 2 or count == 3:
        result[count] += 1

# 7B 문제
def status_dictionary(grid):
    # 가로줄 탐색
    result = {1: 0, 2: 0, 3: 0}
    #result_grid = {1: set(), 2: set(), 3: set()}
    for row in range(5):
        count = 0
        for col in range(5):
            if grid[row][col] == '2':
                count += 1
            else:
                if count == 2 or count == 3:
                    result[count] += 1
                    '''
                    if grid[row][col - count - 1] == '0' and grid[row][col] == '0':
                        result_grid[count].add((row, col - count - 1))
                        result_grid[count].add((row, col))
                    if grid[row][col - count - 1] == '1' and grid[row][col] == '0' and col - count <= 1:
                        result_grid[count].add((row, col))
                    if grid[row][col - count - 1] == '0' and grid[row][col] == '1' and col - 1 >= 3:
                        result_grid[count].add((row, col - count - 1))
                        ''' # c 만들려다가 던짐 - 주석부분은 무시하기
                count = 0
        if count == 2 or count == 3: # 맨 끝자리에서 2로 끝나게되면, 누락되는 부분이 발생하므로 해당 부분을 추가하여 마지막까지 체크함
            result[count] += 1
            '''
            if grid[row][col - count - 1] == '0' and grid[row][col] == '0':
                result_grid[count].add((row, col - count - 1))
                result_grid[count].add((row, col))
            if grid[row][col - count - 1] == '1' and grid[row][col] == '0' and col - count <= 1:
                result_grid[count].add((row, col))
            if grid[row][col - count - 1] == '0' and grid[row][col] == '1' and col - 1 >= 3:
                result_grid[count].add((row, col - count - 1))
                ''' # c 만들려다가 던짐 - 주석부분은 무시하기
    # 세로줄 탐색
    for col in range(5):
        count = 0
        for row in range(5):
            if grid[row][col] == '2':
                count += 1
            else:
                if count == 2 or count == 3:
                    result[count] += 1
                    '''
                    if grid[row - count - 1][col] == '0' and grid[row][col] == '0':
                        result_grid[count].add((row - count - 1, col))
                        result_grid[count].add((row, col))
                    if grid[row - count - 1][col] == '1' and grid[row][col] == '0' and row - count <= 1:
                        result_grid[count].add((row, col))
                    if grid[row - count - 1][col] == '0' and grid[row][col] == '1' and row - 1 >= 3:
                        result_grid[count].add((row - count - 1, col))
                        ''' # c 만들려다가 던짐 - 주석부분은 무시하기
                count = 0
        if count == 2 or count == 3:
            result[count] += 1
            '''
            if grid[row - count - 1][col] == '0' and grid[row][col] == '0':
                result_grid[count].add((row - count - 1, col))
                result_grid[count].add((row, col))
            if grid[row - count - 1][col] == '1' and grid[row][col] == '0' and row - count <= 1:
                result_grid[count].add((row, col))
            if grid[row - count - 1][col] == '0' and grid[row][col] == '1' and row - 1 >= 3:
                result_grid[count].add((row - count - 1, col))
                ''' # c 만들려다가 던짐 - 주석부분은 무시하기
    # 대각선 탐색
    for i in range(1, 5):
        status_dictionary_diagonal(0, i, grid, result, "left_down")
    for i in range(1, 4):
        status_dictionary_diagonal(i, 4, grid, result, "left_down")
    for i in range(3, -1, -1):
        status_dictionary_diagonal(i, 0, grid, result, "right_down")
    for i in range(1, 4):
        status_dictionary_diagonal(0, i, grid, result, "right_down")
    # 1개인 경우는 논외로 탐색
    for row in range(5):
        for col in range(5):
            if grid[row][col] == '2':
                count = 1
                for i in range(row - 1, row + 2):
                    for j in range(col - 1, col + 2):
                        if i >= 0 and i <= 4 and j >= 0 and j <= 4 and (row != i or col != j):
                            if grid[i][j] == '2':
                                count = 0
                result[1] += count
    return result

def best_position_of_my_turn(grid):
    defense = positions_to_avoid_losing(grid) # 무조건 수비해야되는 지점이 있는지 찾기
    if defense != set():
        defense = list(defense)
        return defense[0]
    else:
        attack = status_dictionary(grid) # 수비해야되는 지점이 없으면 공격지점 찾기
        # 닷지요 낄낄낄낄낄

row0 = input("첫 번째 줄 입력: ")
row1 = input("두 번째 줄 입력: ")
row2 = input("세 번째 줄 입력: ")
row3 = input("네 번째 줄 입력: ")
row4 = input("다섯 번째 줄 입력: ")

grid = [row0, row1, row2, row3, row4]
print(grid) # 확인용
print(positions_to_avoid_losing(grid))
print(status_dictionary(grid))
print(best_position_of_my_turn(grid))
