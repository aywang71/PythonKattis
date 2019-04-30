#https://open.kattis.com/problems/oddities
#input format
n = int(input())
#storage values
l  = []
#adds n amount of x to l
for i in range (0,n):
  i += 1
  x = int(input())
  l.append(x)

  
#output format  
for i in range (0,n):
  if l[i]%2 == 0:
    print( l[i], "is even")
  else:
    print( l[i] ,"is odd")
