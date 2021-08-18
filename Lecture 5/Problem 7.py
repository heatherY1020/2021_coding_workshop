import copy

# def display(grid):
#     print('===========================')
#     for y in grid:
#         for x in y:
#             print(x, end='')
#         print('\n', end='')
#     print('===========================')

def getFlow(grid):
    result = copy.deepcopy(grid)
    for y in range(10):
        for x in range(10):
            if (grid[y][x] == '*') or (grid[y][x] == '@'):
                if (y-1 >= 0) and (grid[y-1][x] == '#'):
                    result[y-1][x] = '*'
                if (y+1 <= 9) and (grid[y+1][x] == '#'):
                    result[y+1][x] = '*'
                if (x-1 >= 0) and (grid[y][x-1] == '#'):
                    result[y][x-1] = '*'
                if (x+1 <= 9) and (grid[y][x+1] == '#'):
                    result[y][x+1] = '*'
    return result

city = []
for k in range(10):
    city.append(list(input()))

# display(city)

city = getFlow(city)
# display(city)
city = getFlow(city)
# display(city)
city = getFlow(city)
# display(city)
city = getFlow(city)
# display(city)
city = getFlow(city)
# display(city)

sum = 0
for c in city:
    for s in c:
        if s == '*':
            sum += 1

print(sum)