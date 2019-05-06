#https://open.kattis.com/problems/romans
import math
#input format
x = float(input())
#converts x to km
x = x * (5280/4854) * 1000
#rounding and output format
if (x - (math.floor(x))) < 0.5:
  print(math.floor(x))
elif (x - (math.floor(x))) >= 0.5:
  print(math.ceil(x))
