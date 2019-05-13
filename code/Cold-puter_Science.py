#https://open.kattis.com/problems/cold
n = int(input())

counter = 0

x = input().split(' ')

for i in range (0,n):
  x[i] = int(x[i])
  if x[i] <0:
    counter +=1
  elif x[i]>=0:
    counter = counter

print(counter)
