line_1 = input("first row :")
line_2 = input("second row :")
line_3 = input("third row :")
line_4 = input("fourth row :")
line_5 = input("fifth row : ")
grid = (line_1, line_2, line_3, line_4, line_5)
#print(grid)

def status_dictionary(grid):

  number_1 = 0
  number_2 = 0
  number_3 = 0  
  monitor = []

  def sigma():
    if 3 in monitor:
      number_3 +=1
    elif 2 in monitor:
      for i in monitor :
        if i == 2 :
          number_2 +=1
    monitor.clear()

#hori
  for row in range(5):
    sum = 0
    for col in range(5):
      if grid[row][col] == '2':
        sum += 1
      else : 
        sum = 0
      monitor.append(sum)
      sigma()

#verti
  for col in range(5):
    sum = 0
    for row in range(5):
      if grid[row][col] == '2':
        sum += 1
      else : 
        sum = 0
      monitor.append(sum)
      sigma()

#diag       
  for col in range(5):
    sum = 0
    for frm in range(5-col):
      if grid[0+frm][col+frm] =='2':
        sum +=1
      else:
        sum = 0
      monitor.append(sum)
      sigma()
      
    for frm in range(col):
      if grid[0+frm][col-frm] =='2':
        sum +=1
      else:
        sum = 0
      monitor.append(sum)
      sigma()
    
  for col in range(0, 5, 4):
    for row in range(1, 4):
      sum = 0
      for frm in range(5-row):
        if grid[row+frm][col+frm] =='2':
          sum +=1
        else : 
          sum = 0
        monitor.append(sum)
        sigma()

        if grid[row+frm][col-frm] == '2' :
         sum +=1
        else:
          sum = 0
        monitor.append(sum)
        sigma()

#single detector
  for row in range(5):
    for col in range(5):
      surround = []
      if grid[row][col] =='2':
        surr_index = [(row-1, col-1), (row-1, col), (row-1, col+1), (row, col-1), (row, col), (row, col+1), (row+1, col-1), (row+1, col), (row+1, col+1)]
        for (a, b) in surr_index:
          if a>=0 and a<=4 and b>=0 and b<=4 :
            surround.append(grid[a][b])
        if '2' not in surround:
          number_1 +=1
  print(number_1)
  print(number_2)
  print(number_3)
  print({1 : number_1, 2 : number_2, 3 : number_3})

status_dictionary(grid)
