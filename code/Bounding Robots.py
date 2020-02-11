#https://open.kattis.com/problems/boundingrobots

#inputs until break
while True:
  #input for max room size
  coordinate_max = input().split(' ')
  coordinate_robot = [0,0]
  coordinate_real = [0,0]
  #0,0 is breaker
  if coordinate_max.count('0') == 2:
    break
  else:
    #converts integer
    coordinate_max[0] = int(coordinate_max[0])
    coordinate_max[1] = int(coordinate_max[1])
  #iteration input
  n = int(input())
  for i in range (0,n):
    #gets polar coordinate
    direction, distance = input().split(' ')
    distance = int(distance)
    #complex if statement to change values on actual/ robot
    if direction == 'u':
      coordinate_robot[1] += distance
      coordinate_real[1] += distance
      if coordinate_real[1] >= coordinate_max[1]:
        coordinate_real[1] = coordinate_max[1] -1
    elif direction == 'd':
      coordinate_robot[1] -= distance
      coordinate_real[1] -= distance
      if coordinate_real[1] < 0:
        coordinate_real[1] = 0
    elif direction == 'r':
      coordinate_robot[0] += distance
      coordinate_real[0] += distance
      if coordinate_real[0] >=coordinate_max[0]:
        coordinate_real[0] = coordinate_max[0] -1
    else:
      coordinate_robot[0] -= distance
      coordinate_real[0] -= distance
      if coordinate_real[0] < 0:
        coordinate_real[0] = 0
#output 
  print('Robot thinks %i %i'%(coordinate_robot[0],coordinate_robot[1]))
  print('Actually at %i %i'%(coordinate_real[0],coordinate_real[1]))
