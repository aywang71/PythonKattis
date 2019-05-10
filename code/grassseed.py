#https://open.kattis.com/problems/grassseed
c = float(input())
lawns = int(input())
cost = 0
area = 0
total = 0
for x in range (0,lawns):
  a,b = input().split()
  a = float(a)
  b = float(b)
  area = a * b
  cost = c * area
  total += cost

print(total)
