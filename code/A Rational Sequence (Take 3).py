#https://open.kattis.com/problems/rationalsequence3

#iteration input
n = int(input())
for i in range (n):
  #more input
  case, item = (int(x) for x in input().split(' '))
  # variables for level, how many left/right decisions we make, and count, the beginning node number at the level
  level, count = 0,1
  #finds the level and count
  while count*2 <= item:
    count = count * 2
    level = level + 1
  #debugging
  #print('count:',count)
  #print('level:',level)
  #list moves, for pathfinding
  #records left/right node paths
  moves = []
  #sets up bounds
  left, right = 0,count
  #sets item to a distance from right
  item = item-count
  #until they are within 1 value
  while left + 1 != right:
    #wether or not the item is closer to left or right
    if item < (left+right)//2:
      moves.append('L')
      right = (left+right)//2
    else:
      moves.append('R')
      left = (left+right)//2
  #the output fraction, but as integers in a list
  output = [1,1]
  for i in moves:
    if i == 'L':
      output = [output[0],output[0]+output[1]]
    else:
      output = [output[0]+output[1],output[1]]
  output = [str(output[0]),str(output[1])]
  #output
  print(case,'/'.join(output))
