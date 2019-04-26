#https://open.kattis.com/problems/spavanac
#input format
h,m=input().split()
#convert to integer
h = int(h)
m= int(m)
#storage values
n = 45
#converts to 45 minutes ealier and output format
if m <45:
  if h == 0:
    h = 23
    n = n-m
    m = 60-n
    print(h, m)
  else:
    h = h-1
    n = n-m
    m = 60 - n
    print(h, m)
else:
  m = m-n
  print(h, m)
