#https://open.kattis.com/problems/halfacookie

#import sys for eof
import sys
#import math for sqrt
import math

#a function to find the distance between two points
def distance (x1,y1,x2,y2):
  x = (x2-x1)**2
  y = (y2-y1)**2
  return (math.sqrt(x+y))

def pythag (hyp,s2):
  return math.sqrt((hyp**2)-(s2**2))


#input which reads eof
for line in sys.stdin:
  radius,x,y = (float(x) for x in line.split(' '))
  if (x**2) + (y**2) >= (radius**2):
    print('miss')
    continue
  sides = [radius,0,0]
  #Find distance to x,y
  sides[1] = distance(0,0,x,y)
  #pythagorean theorem to find third side of triangle
  sides[2] = pythag(radius,sides[1])*2
  #sin-1 because we already know the side lengths of the triangle
  central = 2 * (math.degrees(math.acos(sides[1]/sides[0])))
  #print('central angle:',central)
  #find the area of the slice as a portion of the total area
  sarea = central/360 * math.pi * (radius**2)
  #print('slice area:',sarea)
  area = math.pi * (radius**2)
  #print('area:',area)
  #subtract area of triangle from area of slice
  output = [area-(sarea - (sides[2]*sides[1]/2)),sarea - (sides[2]*sides[1]/2)]
  print(max(output),min(output))
  
