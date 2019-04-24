#https://open.kattis.com/problems/trik
#input format
x = str(input())
#storage values
b = len(x)
list(x)
c = 1
#output format
for i in range (0,b):
  if  c == 1:
    if x[i] == 'A':
      c = 2
    elif x[i] == 'B':
      c = 1
    elif x[i] == 'C':
      c = 3
  elif c == 2:
    if x[i] == 'A':
      c = 1
    elif x[i] == 'B':
      c = 3
    elif x[i] == 'C':
      c = 2
  elif c == 3:
    if x[i] == 'A':
      c = 3
    elif x[i] == 'B':
      c = 2
    elif x[i] == 'C':
      c = 1
print(c)
