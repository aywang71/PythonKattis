#https://open.kattis.com/problems/nastyhacks
#input format
n = int(input())
#storage values
i = 1
b = 1
l = []
#appends n number of x's
while i <= n:
  i +=1
  x = input().split()
  l.append(x)
#nested list to convert values
for i in range(0,n):
  for b in range (0,3):
    l[i][b] = float(l[i][b])
  
#output profit identifier, output format  
for i in range(0,n):
  if (l[i][-2] - l[i][-1]) < l[i][0]:
    print('do not advertise')
  elif (l[i][-2] - l[i][-1]) >l[i][0]:
    print('advertise')
  elif (l[i][-2] - l[i][-1]) == l[i][0]:
    print('does not matter')



