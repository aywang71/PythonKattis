#https://open.kattis.com/problems/tram

n = int(input())

distance = 0

for i in range(n):
  point = input().split(' ')
  if int(point[0]) > int(point[1]): distance -= (int(point[0]) - int(point[1]))
  elif int(point[1]) > int(point[0]): distance += (int(point[1]) - int(point[0]))
  #if they are equal they cannot contribute to the difference

shift = distance/n
print(shift)