#https://open.kattis.com/problems/nineknights

#checks if coordinates are in the boundary
def correct (x,y):
  return (0<=x<5) and (0<=y<5)
#runs through all functions
def allpos(grid,x,y):
  if pos1(grid,x,y) or pos2(grid,x,y) or pos3(grid,x,y) or pos4(grid,x,y) or pos5(grid,x,y) or pos6(grid,x,y) or pos7(grid,x,y) or pos8(grid,x,y):
    return False
  return True
#8 functions to measure positions
def pos1(grid,x,y):
  if correct(x-2,y-1) and (grid[x-2][y-1]== 'k'):
    return True
  return False
def pos2(grid,x,y):
  if correct(x-1,y-2) and (grid[x-1][y-2]== 'k'):
    return True
  return False
def pos3(grid,x,y):
  if correct(x+1,y-2) and (grid[x+1][y-2]== 'k'):
    return True
  return False
def pos4(grid,x,y):
  if correct(x+2,y-1) and (grid[x+2][y-1]== 'k'):
    return True
  return False
def pos5(grid,x,y):
  if correct(x+2,y+1) and (grid[x+2][y+1]== 'k'):
    return True
  return False
def pos6(grid,x,y):
  if correct(x+1,y+2) and (grid[x+1][y+2]== 'k'):
    return True
  return False
def pos7(grid,x,y):
  if correct(x-1,y+2) and (grid[x-1][y+2]== 'k'):
    return True
  return False
def pos8(grid,x,y):
  if correct(x-2,y+1) and (grid[x-2][y+1]== 'k'):
    return True
  return False

#booleans
grid = []
count = 0
cont = True
output = True
#input format
for i in range (0,5):
  row = list(input())
  grid.append(row)
  count += row.count('k')
#debugging
print(count)
#only if 9 horses
if count != 9:
  cont = False
  output = False
  print('invalid')
#goes through and checks all horses
if cont == True:
  for x in range (0,5):
    for y in range (0,5):
      if grid[x][y] == 'k':
        if allpos(grid,x,y):
          continue
        else:
          print('invalid')
          output = False
          break
    if output == False:
      break
#final output
if output == True:
  print('valid')
