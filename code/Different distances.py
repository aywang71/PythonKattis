#https://open.kattis.com/problems/differentdistances

#infinite loop
while True:
  points = input().split(' ')
  #only one thing was input; a 0
  if len(points) == 1:
    break
  #data format
  a = float(points[0])
  b = float(points[1])
  c = float(points[2])
  d = float(points[3])
  p = float(points[4])
  #output formula
  print(((abs(a-c)**p)+(abs(b-d)**p))**(1/p))