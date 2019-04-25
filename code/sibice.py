#https://open.kattis.com/problems/sibice
import math
#input format
n,w,h = input().split()
#conversion to integer
n = int(n)
w = int(w)
h = int(h)
#storage values
i = 1
y = []
b = math.sqrt((w*w)+(h*h))
#inputs n x's to list y
while i<=n:
  i += 1
  x = input()
  x = int(x)
  y.append(x)
  #output format, compares x values in list y
for i in y:
  if i<=w:
    print('DA')
  elif i<=h:
    print('DA')
  elif i<=b:
    print('DA')
  else:
    print('NE')
