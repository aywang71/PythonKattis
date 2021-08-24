#https://open.kattis.com/problems/humancannonball2

#imports math
import math
#input format of n
n = int(input())
#declares storage values
safety = []
#asks for n range of five inputs
for i in range (0,n):
  velocity, angle, distance, height1, height2 = input().split(' ')
  #resets time 
  time = 0
  #converts inputs for floats
  velocity = float(velocity)
  angle = float(angle)
  distance = float(distance)
  height1 = float(height1)
  height2 = float(height2)
  #formula for time
  time = (distance)/(velocity*math.cos(math.radians(angle)))
  #debugging
  print(time)
  #formula for finding height given time
  height_time = (velocity*time*math.sin(math.radians(angle))) - (0.5 *9.81*(time*time))
  #debugging
  print(height_time)
  #safety
  safe_interval = (height2-1) - (height1+1)
  #appends safeties to list
  if height_time > (height1+1) and height_time < (height2 -1):
    safety.append("Safe")
  else:
    safety.append("Not Safe")
#debugging
print(safety)
#output format
for i in range (0,len(safety)):
  print(safety[i])