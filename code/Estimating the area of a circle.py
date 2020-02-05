#https://open.kattis.com/problems/estimatingtheareaofacircle

#imports math
import math
#while true
while True:
  #input and data conversion
  radius,total_points,selected_points = input().split()
  radius = float(radius)
  total_points = int(total_points)
  selected_points = int(selected_points)
  #break
  if (radius==0) and (total_points==0) and (selected_points==0):
    break
  #calculations
  square_area = (radius*2)*(radius*2)
  real_circle_area = math.pi * radius *radius
  estimated_circle_area = (selected_points/total_points)*square_area
  #output
  print(real_circle_area,estimated_circle_area)
