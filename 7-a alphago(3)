# 대각선 탐색 함수(7A용)
def positions_to_avoid_losing_diagonal(r, c, grid, result, mode):
    dia_to_row = ""
    row = r # 탐색 시작점
    col = c # 탐색 시작점
    while (row >= 0 and row <= 4 and col >= 0 and col <= 4):
        dia_to_row += grid[row][col]
        row += 1
        if mode == "left_down": # 왼쪽 아래방향으로 탐색
            col -= 1
        elif mode == "right_down": # 오른쪽 아래방향으로 탐색
            col += 1
    row = r
    col = c
    for check in ["0111", "1011", "1101", "1110"]:
        find_index = dia_to_row.find(check)
        if find_index != -1: # find(): 찾은게 없으면 -1을 반환함 -> -1이 아니면 패턴을 찾았다는 뜻
            if mode == "left_down":
                result.add((row + find_index, col - find_index))
            if mode == "right_down":
                result.add((row + find_index, col + find_index))
        row += 1
        if mode == "left_down":
            col -= 1
        elif mode == "right_down":
            col += 1

# 7A 문제
def positions_to_avoid_losing(grid):
    result = set()
    # 가로줄 탐색
    for row in range(5):
        col = 0
        for check in ["0111", "1011", "1101", "1110"]:
            find_index = grid[row].find(check)
            if find_index != -1:
                result.add((row, col + find_index))
            col += 1
    # 세로줄 탐색
    for col in range(5):
        col_to_row = ""
        for row in range(5):
            col_to_row += grid[row][col]
        row = 0
        for check in ["0111", "1011", "1101", "1110"]:
            find_index = col_to_row.find(check)
            if find_index != -1:
                result.add((row + find_index, col))
            row += 1
    # 대각선 탐색
    positions_to_avoid_losing_diagonal(0, 3, grid, result, "left_down")
    positions_to_avoid_losing_diagonal(0, 4, grid, result, "left_down")
    positions_to_avoid_losing_diagonal(1, 4, grid, result, "left_down")
    positions_to_avoid_losing_diagonal(1, 0, grid, result, "right_down")
    positions_to_avoid_losing_diagonal(0, 0, grid, result, "right_down")
    positions_to_avoid_losing_diagonal(0, 1, grid, result, "right_down")
    return result
