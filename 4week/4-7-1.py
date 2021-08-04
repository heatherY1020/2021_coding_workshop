line_1 = input("first row :")
line_2 = input("second row :")
line_3 = input("third row :")
line_4 = input("fourth row :")
line_5 = input("fifth row : ")
grid = (line_1, line_2, line_3, line_4, line_5)
#print(grid)
number_1 = 0
number_2 = 0
number_3 = 0

def status_dictionary(grid):

  for row in range(5):
      for col in range(5):
          sum = 0
          if grid[row][col] == '1':
            sum += 1
          else : 
            sum = 0
          if sum == 3:
            number_3 +=1


  for col in range(5):
      for row in range(2):
          sum = 0
          for frm in range(4):
             if grid[row][col] == '1':
                  sum += 1
             else :
                sum = 0
              if sum == 3:
                for frm in range(4):
                   if grid[row+frm][col] == '0':
                      avoid_losing.append((row+frm, col))
                      
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


avoid_losing = set(avoid_losing)
if len(avoid_losing) == 0:
    print(None)
else:
    for i in avoid_losing:
        print(i)

