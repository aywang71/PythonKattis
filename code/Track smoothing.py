#https://open.kattis.com/problems/tracksmoothing

import math
import copy
n = int(input())
for i in range (n):
  radius, points = (int(x) for x in input().split(" "))
  distance = 0
  point = [int(x) for x in input().split(' ')]
  original = copy.deepcopy(point)
  for j in range(points-1):
    newpoint = [int(x) for x in input().split(' ')]
    distance += math.sqrt(((point[0]-newpoint[0])**2)+((point[1]-newpoint[1])**2) )
    point = copy.deepcopy(newpoint)
  distance += math.sqrt(((point[0]-original[0])**2)+((point[1]-original[1])**2) )
  #print('distance:',distance)
  output = (distance - (2*math.pi*radius))/distance
  #print('output:',output)
  if output < 0:
    print('not possible')
  else:
    print(output)

    

