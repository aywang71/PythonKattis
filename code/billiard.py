#https://open.kattis.com/problems/billiard

#needed for tan and square root
import math

def speed (x,y,time,horizontal,vertical):
  #speed per second in a given direction
  left = y *vertical/time
  right = x*horizontal/time
  #debugging
  print(left,right)
  #distance is through pythagorean theorm
  distance = (math.sqrt(right**2+left**2))
  #output
  return left,right,distance

#until input of 0 0 0 0 0
while True:
  #input
  values = input().split(' ')
  #break point
  if values.count('0') == 5:
    break
  #conversion to integer
  for i in range (0,len(values)):
    values[i] = int(values[i])
  #finds speed
  left,right,velocity = speed(values[0],values[1],values[2],values[3],values[4])
  #Finds the angle through reverse tangent
  angle = round(math.degrees(math.atan(left/right)),2)
  velocity = round(velocity,2)
  #debugging
  print('velocity:',velocity)
  print('angle:',angle)

  #if/elif statements to add or take away 0s at the end for output
  if len(str(angle).split('.')[1]) < 2:
    x = list(str(angle))
    x.append('0')
    angle = ''.join(x)
  elif len(str(angle)) > 5:
    angle = str(angle).strip('0')

  if len(str(velocity).split('.')[1]) < 2:
    x = list(str(velocity))
    x.append('0')
    velocity = ''.join(x)
  elif len(str(velocity)) > 5:
    velocity = str(velocity).strip('0')
  #output
  print(angle,velocity)
