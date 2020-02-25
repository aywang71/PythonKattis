#https://open.kattis.com/problems/pervasiveheartmonitor

import sys

#input format using EOF
for line in sys.stdin:
  sep = line.split(' ')
  numbers = []
  name = []
  #tries to convert to integer, or appends to name list
  for i in range (0,len(sep)):
    try:
      sep[i] = float(sep[i])
      numbers.append(sep[i])
    except ValueError:
      name.append(sep[i])
  #debugging
  print(name)
  print(numbers)
  #output format
  name = ' '.join(name)
  avg = (sum(numbers))/(len(numbers))
  print(avg,name)
#traditional input
'''
n = int(input())
for i in range (0,n):
  sep = input().split(' ')
  numbers = []
  name = []
  for i in range (0,len(sep)):
    try:
      sep[i] = float(sep[i])
      numbers.append(sep[i])
    except ValueError:
      name.append(sep[i])
  #print(name)
  #print(numbers)
  name = ' '.join(name)
  avg = (sum(numbers))/(len(numbers))
  print(avg,name)
  '''