#https://open.kattis.com/problems/unlockpattern

#for sqrt function
import math
#function to find distance
def dis(prev,cur):
  x = abs(prev[0]-cur[0])
  y = abs(prev[1]-cur[1])
  fin = math.sqrt((x*x)+(y*y))
  #debugging
  print('distsance:',fin)
  return fin

grid = []
distance = 0
#input for grid array
for i in range (0,3):
  row = input().split(' ')
  for i in range (0,3):
    row[i] = int(row[i])
  grid.append(row)
#debugging
print('grid:',grid)
#finds 1, the first previous value
for i in range(0,len(grid)):
  if 1 in grid[i]:
    x = grid[i]
    previous =[i,(x.index(1))]
#first for loop is to cover the numbers 2-10
for i in range (2,10):
  #this goes through to find the number (i)
  for j in range(0,len(grid)):
    if i in grid[j]:
      #sets up for index function
      x = grid[j]
      #uses list format [x,y] 
      current = [j,x.index(i)]
      #debugging
      print(current)
      #adds to distance
      distance += dis(previous,current)
      #sets current to previous
      previous = current
#output
print(distance)


