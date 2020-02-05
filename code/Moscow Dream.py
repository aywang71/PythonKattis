#input
problems = [int(i) for i in input().split(' ')]
#boolean for rule testing
cont = True

#if any of the problems are 0
if (problems[0] == 0) or (problems[1] == 0) or (problems[2] == 0):
  cont = False
  print('NO')

#if the total is less than the amount needed
if (sum(problems[0:3]) < problems[3]) and (cont == True):
  cont = False
  print('NO')

#if the needed problems is less than 3
if (problems[3] < 3) and (cont == True):
  cont = False
  print('NO')

#final output
if cont:
  print('YES')