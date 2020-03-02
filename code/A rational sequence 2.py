#https://open.kattis.com/problems/rationalsequence2

#finds where x began
def root (x):
  count = 0
  movement = []
  summed = [1]
  num,den = x.split('/')
  num = int(num)
  den = int(den)
  while (num != 1) or (den != 1):
    count += 1
    summed.append(2**len(summed))
    if num > den:
      movement.append('R')
      num -= den
    elif den > num:
      movement.append('L')
      den -= num
  movement = movement[::-1]
  summed.pop(-1)
  return count,movement,summed

def find (count,movement,summed):
  if count == 0:
    return 1
  row = [1,2**count]
  for i in range(len(movement)-1):
    if movement[i] == "L":
      row = [row[0],row[0]+(row[1]-row[0])//2]
    elif movement[i] == "R":
      row = [row[0]+(row[1]-row[0]+1)//2,row[1]]
    #print('Row:',row)
  if movement[-1] == "L":
    return row[0] + sum(summed)
  elif movement[-1] == "R":
    return row[1] + sum(summed)

n = int(input())
for i in range (n):
  case,number = input().split(' ')
  count,movement,summed = root(number)
  #print(movement)
  #print(count)
  #print('summed:',summed)
  placement = find(count,movement,summed)
  print(case,int(placement))
