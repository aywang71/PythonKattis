#https://open.kattis.com/problems/mirror

#iteration input
n = int(input())
#loop through
for i in range (0,n):
  #first output
  print('Test',i+1)
  #more inptu
  rows, columns = input().split(' ')
  rows = int(rows)
  columns = int(columns)
  grid = []
  #input for virtual grid
  for x in range (0,rows):
    row = list(input())
    grid.append(row)
  #debugging
  print(grid)
  #output format
  for x in range (rows-1,-1,-1):
    #debugging
    print(i)
    x = grid[x]
    x.reverse()
    print(''.join(x))