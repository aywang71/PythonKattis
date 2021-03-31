def time(total):
  h = total%60
  #print('hours',h)
  m = total//60
  #print('minutes',m)
  return h,m
h,m=input().split()
h = int(h)
m= int(m)
total = h*60 + m - 45
#print('total',total)
m,h = time(total)
#print('out',h)
#print('out',m)
if h < 0:
  h = 23
print(h,m)