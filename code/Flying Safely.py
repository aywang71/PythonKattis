#https://open.kattis.com/problems/flyingsafely

#iteration inptu
n = int(input())
for i in range (0,n):
  cities, pilots = input().split(' ')
  cities = int(cities)
  pilots = int(pilots)
  #this part doesn't really matter but we need inputs
  for i in range (0,pilots):
    city1, city2 = input().split(' ')
  #output
  print(cities-1)
    