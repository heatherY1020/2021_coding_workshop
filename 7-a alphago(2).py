line_1 = input("first row :")
line_2 = input("second row :")
line_3 = input("third row :")
line_4 = input("fourth row :")
line_5 = input("fifth row : ")
grid = (line_1, line_2, line_3, line_4, line_5)
#print(grid)
avoid_losing = []

def hori():
  for row in range(5):
      for col in range(2):
          sum = 0
          for frm in range(4):
              if grid[row][col+frm] == '1':
                  sum += 1
          if sum == 3:
              for frm in range(4):
                  if grid[row][col+frm] == '0':
                      avoid_losing.append((row, col+frm))
def verti():
  for col in range(5):
      for row in range(2):
          sum = 0
          for frm in range(4):
              if grid[row+frm][col] == '1':
                  sum += 1
          if sum == 3:
              for frm in range(4):
                  if grid[row+frm][col] == '0':
                      avoid_losing.append((row+frm, col))
def diag():
  for row in range(2):
      for col in range(2):
          sum = 0
          for frm in range(4):
              if grid[row+frm][col+frm] == '1':
                  sum += 1
          if sum == 3:
              for frm in range(4):
                  if grid[row+frm][col+frm] == '0':
                      result.append((row+frm, col+frm))
      for col in range(3, 5):
          sum = 0
          for frm in range(4):
              if grid[row+frm][col-frm] == '1':
                  sum += 1
          if sum == 3:
              for frm in range(4):
                  if grid[row+frm][col-frm] == '0':
                      result.append((row+frm, col-frm))

hori()
verti()
diag()

avoid_losing = set(avoid_losing)
if len(avoid_losing) == 0:
    print(None)
else:
    for i in avoid_losing:
        print(i)

