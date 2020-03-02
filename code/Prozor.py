#https://open.kattis.com/problems/prozor

#import for sqrt
import math
#deepcopies needed to be able to refer to original
import copy

#function to output the grid
def out (grid):
  for i in grid:
    print(''.join(i))

#makes a rectangle and formats properly
def find (net,flyswat,x,y):
  grid = copy.deepcopy(net)
  grid[x][y] = '+'
  grid[x][y+flyswat-1] = '+'
  grid[x+flyswat-1][y] = '+'
  grid[x+flyswat-1][y+flyswat-1] = '+'
  #out(grid)
  for i in range (1,flyswat-1):
    grid[x][y+i] = '-'
    grid[x+flyswat-1][y+i] = '-'
    grid[x+i][y] = '|'
    grid[x+i][y+flyswat-1] = '|'
  return grid

#counts the flies in the rectangle
def count(updated,x,y,flyswat):
  flies = 0
  #goes through range but eliminates the border
  for i in range (x+1,x+flyswat-1):
    for j in range (y+1,y+flyswat-1):
      if updated[i][j] == '*':
        #debugging
        print('i:',i,'j:',j)
        flies += 1
  #debugging
  print('flies:',flies)
  return flies

#input
rows, columns, flyswat = input().split(' ')
grid = []
best = []
orig = 0
#data formatting
rows = int(rows)
columns = int(columns)
flyswat = int(flyswat)
#forms grid
for i in range (rows):
  row = list(input())
  grid.append(row)
#we measure the point from the upper left
for x in range (rows-flyswat+1):
  for y in range (columns-flyswat+1):
    #we want to count the flies first to save processing power
    flies = count(grid,x,y,flyswat)
    if flies > orig:
      best = find(grid,flyswat,x,y)
      #debugging
      print('new:')
      out(best)
      orig = flies
#debugging
print(best)
print(orig)
out(best)