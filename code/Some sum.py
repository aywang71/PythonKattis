#https://open.kattis.com/problems/somesum
import math

n = int(input())

x = n%2

if x == 0:
  #debugging
  print(math.log(n,2))
  if math.log(n,2) == math.floor(math.log(n,2)):
    if math.log(n,2) == 1.0:
      print('Odd')
    else:
      print('Even')
  else:
    print('Odd')
else:
  print('Either')