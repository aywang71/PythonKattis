#https://open.kattis.com/problems/jewelrybox

import math
def quad (l,w):
  b = -4*l -4*w
  c = l*w
  x = (-b + math.sqrt(b**2 - (48*c)))/24
  y = (-b - math.sqrt(b**2 - (48*c)))/24
  vol1 = x*(l-2*x)*(w-2*x)
  vol2 = y*(l-2*y)*(w-2*y)
  #print(vol1,vol2)
  return max(vol1,vol2)
n = int(input())
for i in range (n):
  l,w = (int(x) for x in input().split(' '))
  print(quad(l,w))

