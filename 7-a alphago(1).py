#7
line_1 = input("first row :")
line_2 = input("second row :")
line_3 = input("third row :")
line_4 = input("fourth row :")
line_5 = input("fifth row : ")
current_situation = (line_1, line_2, line_3, line_4, line_5)
#print(current_situation)
error_situation = []
answer_list = []

def hori():
  for i in range(5):
    danger_number = 0
    for idj, j in enumerate(current_situation[i]):
      if j =="1":
        danger_number +=1
      else :
        danger_number =0
      #연속이 아니라면 danger_number는 다시금 0으로 돌아감.
      #print(danger_number)

      if danger_number ==2:
        if (idj==1) or (idj==2):
          if (current_situation[i][idj+1]=="0") and (current_situation[i][idj+2]=="1"):
            answer_list.append((i, idj+1))
            error_situation.append("True")

        elif (idj==3) or (idj ==4):
          if (current_situation[i][idj-2]=="0") and (current_situation[i][idj-3]=="1"):
            answer_list.append((i, idj-2))
            error_situation.append("True")
        #horizontal에서 2-1로 건너뛰어 4가 되는 것을 막아준다.

      elif danger_number ==3:
        if (idj==2) and (current_situation[i][3] != "2"):
          answer_list.append((i, 3))
          error_situation.append("True")
        elif idj==3:
          if current_situation[i][4] != "2":
            answer_list.append((i, 4))
            error_situation.append("True")
          if current_situation[i][0] != "2":
            answer_list.append((i, 0))
            error_situation.append("True")
        elif idj ==4:
          if current_situation[i][1] != "2":
            answer_list.append((i, 1))
            error_situation.append("True")
       #horizontal에서 3개짜리일때 양옆을 막아준다.

hori()

def verti():
  for i in range(5):
    danger_number = 0
    for j in range(5):
      k=current_situation[j][i]
      #j와 i의 순서를 바꾸게 되면 column이 고정되고 먼저 행이 돈다.
      if k=="1":
        danger_number +=1
      else:
        danger_number =0
      #연속이 아니라면 danger_number는 다시금 0으로 돌아감.

      if danger_number ==2:
        if (j ==1) or (j==2):
          if (current_situation[j+1][i]=="0") and (current_situation[j+2][i]=="1"):
            answer_list.append((j+1, i))
            error_situation.append("True")
        elif (j==3) or (j==4):
          if (current_situation[j-2][i]=="0") and (current_situation[j-3][i]=="1"):
            answer_list.append((j-2, i))
            error_situation.append("True")
      #vertical에서 2-1로 건너뛰어 4가 되는 것을 막아준다.

      elif danger_number ==3:
        if j ==2:
          if current_situation[3][i] != "2":
            answer_list.append((3, i))
            error_situation.append("True")
        if j==3:
          if current_situation[0][i] != "2":
            answer_list.append((0, i))
            error_situation.append("True")
          if current_situation[4][i] != "2":
            answer_list.append((4, i))
            error_situation.append("True")
        if j==4:
          if current_situation[1][i] != "2":
            answer_list.append((1, i))
            error_situation.append("True")
      #vertical에서 3개짜리일때 양옆을 막아준다.

verti()

def diag_large():
  danger_number1 = 0
  danger_number2 = 0
  for i in range(5):
    j = current_situation[i][i]
    k = current_situation[i][4-i]
    if j == "1":
      danger_number1 +=1
    else :
      danger_number1 =0
    
    if k =="1":
      danger_number2 +=1
    else :
      danger_number2 =0
    #5칸짜리 대각선을 병렬적으로 동시에 돌릴 생각.

    if danger_number1 ==2:
      if (i ==1) or (i==2):
        if (current_situation[i+1][i+1]=="0") and (current_situation[i+2][i+2]=="1"):
          answer_list.append((i+1, i+1))
          error_situation.append("True")
      elif (i==3) or (i==4):
        if (current_situation[i-2][i-2]=="0") and (current_situation[i-3][i-3]=="0"):
          answer_list.append((i-2, i-2))
          error_situation.append("True")
    #5칸짜리 diagonal에서 2-1로 건너뛰어 4가 되는 것을 막아준다.

    elif danger_number1 ==3:
      if i ==2:
        if current_situation[3][3] != "2":
          answer_list.append((3, 3))
          error_situation.append("True")
      if i==3:
        if current_situation[0][0] != "2":
          answer_list.append((0, 0))
          error_situation.append("True")
        if current_situation[4][4] != "2":
          answer_list.append((4, 4))
          error_situation.append("True")
      if i==4:
        if current_situation[1][1] != "2":
          answer_list.append((1, 1))
          error_situation.append("True")
    #5칸짜리 diagonal에서 3개짜리일때 양대각선을 막아준다.

    if danger_number2 ==2:
      if (i ==1) or (i==2):
        if (current_situation[i+1][4-(i+1)]=="0") and (current_situation[i+2][4-(i+2)]=="1"):
          answer_list.append((i+1, 4-(i+1)))
          error_situation.append("True")
      elif (i==3) or (i==4):
        if (current_situation[i-2][4-(i-2)]=="0") and (current_situation[i-3][4-(i-3)]=="0"):
          answer_list.append((i-2, 4-(i-2)))
          error_situation.append("True")
    #5칸짜리 diagonal에서 2-1로 건너뛰어 4가 되는 것을 막아준다.

    elif danger_number2 ==3:
          if i ==2:
            if current_situation[3][1] != "2":
              answer_list.append((3, 1))
              error_situation.append("True")
          elif i==3:
            if current_situation[0][4] != "2":
              answer_list.append((0, 4))
              error_situation.append("True")
            if current_situation[4][0] != "2" :
              answer_list.append((4, 0))
              error_situation.append("True")
          elif i==4:
            if current_situation[1][3] != "2":
              answer_list.append((1, 3))
              error_situation.append("True")
        #5칸짜리 diagonal에서 3개짜리일때 양대각선을 막아준다.

diag_large()

def diag_small():
  danger_number1 = 0
  danger_number2 = 0
  danger_number3 = 0
  danger_number4 = 0
  danger_list = [danger_number1, danger_number2, danger_number3, danger_number4]
  for i in range(4):
    a = current_situation[1+i][i]
    b = current_situation[i][1+i]
    c = current_situation[i][4-(1+i)]
    d = current_situation[1+i][4-i]
    e = [a, b, c, d]

    for idj, j in enumerate(e):
      if j=="1":
        danger_list[idj] +=1
      else:
        danger_list[idj] = 0
      #danger_number1,2,3,4를 각각 upload시킨다.
      
      if danger_list[0] ==2:
        if i==1:
          if (current_situation[3][2]=="0") and (current_situation[4][3]=="1"):
            answer_list.append((3, 2))
            error_situation.append("True")
        elif i==3:
          if (current_situation[2][1]=="0") and (current_situation[0][1]=="1"):
            answer_list.append((2, 1))
            error_situation.append("True")
      elif danger_list[0] ==3:
        if i==2:
          if current_situation[4][3] != "2" :
            answer_list.append((4, 3))
            error_situation.append("True")
        elif i==3:
          if current_situation[1][0] != "2" :
            answer_list.append((1, 0))
            error_situation.append("True")
        #a에 관해서 먼저 검사 끝내고,

      if danger_list[1] ==2:
        if i==1:
          if (current_situation[2][3]=="0") and (current_situation[3][4]=="1") :
            answer_list.append((2, 3))
            error_situation.append("True")
        elif i==3:
          if (current_situation[1][2]=="0") and (current_situation[0][1] =="1") :
            answer_list.append((0, 1))
            error_situation.append("True")
      elif danger_list[1] ==3:
        if i==2:
          if current_situation[3][4] != "2" :
            answer_list.append((3, 4))
            error_situation.append("True")
        elif i==3:
          if current_situation[0][1] != "2" :
            answer_list.append((0, 1))
            error_situation.append("True")
        #b에 관해서 검사를 끝낸다.

      if danger_list[2] ==2:
        if i==1:
          if (current_situation[2][1]=="0") and (current_situation[3][0]=="1") :
            answer_list.append((2, 1))
            error_situation.append("True")
        elif i==3:
          if (current_situation[1][2]=="0") and (current_situation[0][3] =="1") :
            answer_list.append((1, 2))
            error_situation.append("True")
      elif danger_list[2] ==3:
        if i==2:
          if current_situation[3][0] != "2" :
            answer_list.append((3, 0))
            error_situation.append("True")
        elif i==3:
          if current_situation[0][3] != "2" :
            answer_list.append((0, 3))
            error_situation.append("True")
        #c에 관해서 검사를 끝낸다.

      if danger_list[3] ==2:
        if i==1:
          if (current_situation[3][2]=="0") and (current_situation[4][1]=="1") :
            answer_list.append((3, 2))
            error_situation.append("True")
        elif i==3:
          if (current_situation[2][3]=="0") and (current_situation[1][4] =="1") :
            answer_list.append((2, 3))
            error_situation.append("True")
      elif danger_list[3] ==3:
        if i==2:
          if current_situation[4][1] != "2":
            answer_list.append((4, 1))
            error_situation.append("True")
        elif i==3:
          if current_situation[1][4] != "2":
            answer_list.append((1, 4))
            error_situation.append("True")
        #d에 관해서 검사를 끝낸다.

diag_small()  

answer_list = list(set(answer_list))
if "True" not in error_situation:
  print("None")
else:
  for i in answer_list:
    print(i)
