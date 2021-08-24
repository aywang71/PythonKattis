#https://open.kattis.com/problems/secretmessage

#needed for ceil and sqrt
import math
#makes a square from the given string
def square (string):
  #calculates square side lengths
  length = math.ceil(math.sqrt(len(string)))
  output = []
  count = -1
  #debugging
  print(length)
  #nested loop for length ** 2, which allows for construction of square
  for i in range (length):
    row = []
    for i in range (length):
      count += 1
      if count >= len(string):
        row.append('*')
        continue
      row.append(string[count])
    output.append(row)
    #debugging
    print(output)
  return output  

#iteration input
n = int(input())
for i in range (n):
  #more input
  string = list(input())
  grid = square(string)
  #debugging
  print(grid)
  #reverses grid so that our formula can work
  grid = grid[::-1]
  #debugging
  print(grid)
  #epic formula
  grid = list(map("".join,zip(*grid)))
  #replaces
  for i in range(len(grid)):
    x = grid[i].replace('*','')
    grid[i] = x
  #output
  print(''.join(grid))
