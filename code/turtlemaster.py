#https://open.kattis.com/problems/turtlemaster

def move (angle,grid,x,y):
  try:
    #top
    if angle%360 == 0:
      move = grid[x-1][y]
      x -= 1
      if x < 0:
        return x,y,'lose'
      elif move == '.':
        return x,y,'cont'
      elif move == 'D':
        return x,y,'win'
      return x,y,'lose'
    #right
    elif angle%360 == 90:
      move = grid[x][y+1]
      y += 1
      if y > 7:
        return x,y,'lose'
      if move == '.':
        return x,y,'cont'
      elif move == 'D':
        return x,y,'win'
      return x,y,'lose'
    #down
    elif angle%360 == 180:
      move = grid[x+1][y]
      x += 1
      if x > 7:
        return x,y,'lose'
      if move == '.':
        return x,y,'cont'
      elif move == 'D':
        return x,y,'win'
      return x,y,'lose'
    #left
    elif angle%360 == 270:
      move = grid[x][y-1]
      y -= 1
      if y < 0:
        return x,y,'lose'
      elif move == '.':
        return x,y,'cont'
      elif move == 'D':
        return x,y,'win'
      return x,y,'lose'
  except:
    return x,y,'lose'

def melt(angle,grid,x,y):
  try:
    #top
    if angle%360 == 0:
      move = grid[x-1][y]
      if (x-1) < 0:
        return x,y,'lose'
      elif move == 'I':
        grid[x-1][y] = '.'
        return x,y,grid
      else:
        return x,y,'lose'
    #right
    elif angle%360 == 90:
      move = grid[x][y+1]
      if (y+1) > 7:
        return x,y,'lose'
      if move == 'I':
        grid[x][y+1] = '.'
        return x,y,grid
      else:
        return x,y,'lose'
    #down
    elif angle%360 == 180:
      move = grid[x+1][y]
      if (x+1) > 7:
        return x,y,'lose'
      if move == 'I':
        grid[x+1][y] = '.'
        return x,y,grid
      else:
        return x,y,'lose'
    #left
    elif angle%360 == 270:
      move = grid[x][y-1]
      if (y-1) < 0:
        return x,y,'lose'
      elif move == 'I':
        grid[x][y-1] = '.'
        return x,y,grid
      else:
        return x,y,'lose'
  except:
    return x,y,'lose'

x,y = 7,0
boolean = 'cont'
grid = []
angle = 90
for i in range (8):
  row = list(input())
  grid.append(row)
sequence = list(input())
#print(grid)
#print(sequence)

for i in sequence:
  if i == 'F':
    x,y,boolean = move(angle,grid,x,y)
  elif i == 'R':
    angle += 90
  elif i == 'L':
    angle -= 90
  elif i == 'X':
    x,y,grid = melt(angle,grid,x,y)
  #print('x:',x)
  #print('y:',y)
  #print('angle:',angle)
  #print('boolean:',boolean)
  #print('grid:',grid)
  if (boolean == 'lose') or (grid == 'lose'):
    break
if boolean == 'cont'or boolean == 'lose' or grid == 'lose':
  print('Bug!')
if boolean == 'win':
    print('Diamond!')