#https://open.kattis.com/problems/amoebas

#UNTIL ROW 67 IS JUST CHECKING FOR NEARBY '#' ON THE GRID
# all functions follow format of a try-except to check if a "#" is nearby
def dia1 (row,column,grid):
  try:
    if grid[row-1][column-1] == '#':
      if (row-1<0) or (column-1<0):
        return False
      return True
  except:
    pass
  return False
def dia2 (row,column,grid):
  try:
    if grid[row-1][column+1] == '#':
      if (row-1<0):
        return False
      return True
  except:
    pass
  return False
def dia3 (row,column,grid):
  try:
    if grid[row+1][column+1] == '#':
      return True
  except:
    pass
  return False
def dia4 (row,column,grid):
  try:
    if grid[row+1][column-1] == '#':
      if (column-1<0):
        return False
      return True
  except:
    pass
  return False
def str1 (row,column,grid):
  try:
    if grid[row-1][column] == '#':
      if (row-1<0):
        return False
      return True
  except:
    pass
  return False
def str2 (row,column,grid):
  try:
    if grid[row+1][column] == '#':
      return True
  except:
    pass
  return False
def str3 (row,column,grid):
  try:
    if grid[row][column-1] == '#':
      if (column-1<0):
        return False
      return True
  except:
    pass
  return False
def str4 (row,column,grid):
  try:
    if grid[row][column+1] == '#':
      return True
  except:
    pass
  return False

#This function uses functions shown above to find how many '#' are nearby. Once theres only one nearby, it finds, the row/column placement, changes the grid, and returns the values
def find (row,column,grid,first):
  count = 0
  if dia1(row,column,grid):
    count += 1
    #print('dia1')
  if dia2(row,column,grid):
    count += 1
    #print('dia2')
  if dia3(row,column,grid):
    count += 1
    #print('dia3')
  if dia4(row,column,grid):
    count += 1
    #print('dia4')
  if str1(row,column,grid):
    count += 1
    #print('str1')
  if str2(row,column,grid):
    count += 1
    #print('str2')
  if str3(row,column,grid):
    count += 1
    #print('str3')
  if str4(row,column,grid):
    count += 1
    #print('str4')
  #print(row,column)
  #print(count)
  # return portion starts here
  #this portion goes through to adjust the values on the grid and update the row/column status
  if (count == 1) or (first == True):
    if dia1(row,column,grid):
      grid[row][column] = '.'
      row,column = row-1,column-1
      return row,column,grid, True, False
    elif dia2(row,column,grid):
      grid[row][column] = '.'
      row,column = row-1,column+1
      return row,column,grid, True, False
    elif dia3(row,column,grid):
      grid[row][column] = '.'
      row,column = row+1,column+1
      return row,column,grid, True, False
    elif dia4(row,column,grid):
      grid[row][column] = '.'
      row,column = row+1,column-1
      return row,column,grid, True, False
    elif str1(row,column,grid):
      grid[row][column] = '.'
      row= row-1
      return row,column,grid, True, False
    elif str2(row,column,grid):
      grid[row][column] = '.'
      row= row+1
      return row,column,grid, True, False
    elif str3(row,column,grid):
      grid[row][column] = '.'
      column = column -1
      return row,column,grid, True, False
    elif str4(row,column,grid):
      grid[row][column] = '.'
      column = column +1
      return row,column,grid, True, False
  return row,column,grid,False, False

#used to find and replace each '#' in a rectangle
def find_rect (row,column,grid,ult,placeholder):
  count = 1
  first = True
  while placeholder == True:
    row,column,grid,placeholder, first = find(row,column,grid,first)
    #print(row,column)
    count += 1
  #to alter the amoeba count
  if count >2:
    ult += 1
  return row,column,grid,ult
#for debugging purposes
def prgrid(grid):
  for i in grid:
    print(''.join(i))

#input
rows, columns = input().split(' ')
rows = int(rows)
columns = int(columns)
grid = []
#grid input
for i in range (0,rows):
  row = list(input())
  grid.append(row)
#output variable
ult = 0
#used in find_rect and output booleans
placeholder = True
#goes through each item
for i in range (0,rows):
  for x in range (0,columns):
    #if its a "#"
    if grid[i][x] == '#':
      row = i
      column = x
      #runs find_rect function (does everything)
      row,column,grid,ult = find_rect(row,column,grid,ult,placeholder)
      #prgrid(grid)
#output
print(ult)