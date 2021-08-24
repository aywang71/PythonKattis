#https://open.kattis.com/problems/thisaintyourgrandpascheckerboard

def consec_checker(temp_list):
  for i in range(0, len(temp_list)-2):
    if temp_list[i] == temp_list[i+1] and temp_list[i] == temp_list[i+2]:
      return False
  return True

#checks rows are equal numbers
def row_check(board):
  for i in board:
    #debugging
    #print('row:',i)
    if i.count("W") == i.count("B"):
      if consec_checker(i):
        continue
      else:
        return False
      continue
    else:
      return False
  return True

#checks columns are equal numbers
def col_check(board):
  #makes a list out of the column
  for i in range(len(board)):
    temp_list = []
    x = 0 
    #nested loop for making a list from a column
    for j in range (len(board)):
      temp_list.append(board[x][i])
      #increments to next column
      x += 1
    #debugging
    #print('column:',temp_list)
    if temp_list.count("W") == temp_list.count("B"):
      if consec_checker(temp_list):
        continue
      else:
        return False
      continue
    else:
      return False
  return True

#number of rows
cells = int(input())
#debugging
#print('lig')
board = []
#nested board input
for i in range(cells):
  board.append(list(input()))

output = False
if row_check(board) and col_check(board):
  output = True

if output:
  print('1')
else:
  print('0')