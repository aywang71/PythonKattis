#https://open.kattis.com/problems/planina
#input format
n = int(input())
#can't calculate for the first iteration: if loop
if n == 1:
  print(9)
else:
  # if n!= 1, run this loop
  i=3
  #counts each iteration of i in range of x
  for x in range (1,n):
    i = i+(i-1)
    #debugging
    print(i)
  print(i*i)
