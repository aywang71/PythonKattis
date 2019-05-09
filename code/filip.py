#https://open.kattis.com/problems/filip
a,b= input().split()
b = b [::-1]
a = a [::-1]
a = int(a)
b = int(b)
if a>b:
  print(a)
elif b>a:
  print(b)
