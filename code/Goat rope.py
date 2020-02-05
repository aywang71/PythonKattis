#https://open.kattis.com/problems/goatrope

#brings in math library
import math
#gets inputs and converts to proper data type
GoatX, GoatY,X1,Y1,X2,Y2 = input().split(' ')
GoatX = int(GoatX)
GoatY = int(GoatY)
X1 = int(X1)
Y1 = int(Y1)
X2 = int(X2)
Y2 = int(Y2)
#lists for temp storage and totals
compare = []
total_distance = []
#many if statements to find correct direction and distance
if (X1 >GoatX) and (X2 >GoatX):
  compare.append(X1 -GoatX)
  compare.append(X2 - GoatX)
  total_distance.append(min(compare))
compare = []
if (X2 <GoatX) and (X1 < GoatX):
  compare.append(GoatX - X2)
  compare.append(GoatX-X1)
  total_distance.append(min(compare))
compare = []
if (Y2 >GoatY) and (Y1 >GoatY):
  compare.append(Y2-GoatY)
  compare.append(Y1 - GoatY)
  total_distance.append(min(compare))
compare = []
if (Y2<GoatY) and (Y1<GoatY):
  compare.append(GoatY-Y2)
  compare.append(GoatY-Y1)
  total_distance.append(min(compare))
#if theres more than 2 directions, use pt, other wise print it out.
# there could be more than 2 directions if the rectangle was located diagonally from the goat.
if len(total_distance) == 2:
  print(math.sqrt((total_distance[1]**2) + (total_distance[0]**2)))
else:
  print(total_distance[0])