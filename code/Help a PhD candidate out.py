#https://open.kattis.com/problems/helpaphd

#gets n inputs
n = int(input())
#prompts for n inputs
for i in range(0,n):
  #try for catching
  try:
    x,y = input().split("+")
    x = int(x)
    y = int(y)
    print(x+y)
  except:
    print('skipped')