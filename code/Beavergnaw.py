#https://open.kattis.com/problems/beavergnaw

#imported for cube root
import math
#until input 0 0 
while True:
  #input format
  D,V = input().split(' ')
  D = int(D)
  V = int(V)
  if (D== 0) and (V==0):
    break
  #formula
  d = math.pow(((D*D*D)-(6*V/math.pi)),(1/3))
  #output format
  print(d)