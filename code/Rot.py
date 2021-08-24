#https://open.kattis.com/problems/rot

def yxPY (y,x): #in which y to 0 is first - goes on 45 and 225
  out = []
  for i in range(y-1, -1, -1):
    out.append( (i)* ' ')
  for i in range(1, x):
    out.append( (i)* ' ')
  return out
def xyPY (y,x): #in which x to 0 is first - goes on 135 and 315
  out = []
  for i in range(x-1, -1, -1):
    out.append( (i) * ' ')
  for i in range(1,y):
    out.append( (i) * ' ')
  return out

def fourtyfive (y,x,text):
  order = []
  for i in range(y-1):
    row = []
    start = [i,0]
    while (start[0] != -1) and (start[1] != x):
      row.append(text[start[0]][start[1]])
      start[0] -= 1
      start[1] += 1
    order.append(row)
  for i in range(x-1):
    row = []
    start = [y-1,i]
    while (start[0] != -1) and (start[1] != x):
      row.append(text[start[0]][start[1]])
      start[0] -= 1
      start[1] += 1
    order.append(row)
  order.append([text[y-1][x-1]])
  return order

def twentyfive (y,x,text):
  order = fourtyfive(y,x,text)
  order.reverse()
  for i in range(len(order)):
    order[i] = order[i][::-1]
  return order

def fifteen (y,x,text):
  order = []
  for i in range(y-1):
    row = []
    start = [i,x-1]
    while (start[0] != -1) and(start[1] != -1):
      row.append(text[start[0]][start[1]])
      start[0] -= 1
      start[1] -= 1
    order.append(row[::-1])
  for i in range(x-1,-1,-1):
    row = []
    start = [y-1, i]
    while (start[0] != -1) and (start[1] != -1):
      row.append(text[start[0]][start[1]])
      start[0] -= 1
      start[1] -= 1
    order.append(row[::-1])
  return order

def thirtyfive (y,x,text):
  order = fifteen(y,x,text)
  order.reverse()
  for i in range(len(order)):
    order[i] = order[i][::-1]
  return order

def addition (out, order):
  for i in range(len(out)):
    out[i] += order[i][0]
    for x in range(1,len(order[i])):
      out[i] += ' ' + order[i][x]
  return out

def transpose(text):
  out = []
  for i in range(len(text[0])):
    row = []
    for x in range(len(text)):
      row.append(text[x][i])
    out.append(row)
  return out

#input
y, x = input().split(' ')
y = int(y)
x = int(x)
text = []

for i in range(y):
  text.append(list(input()))

degrees = int(input())
out = []

if degrees == 45 or degrees == 225:
  out = yxPY(y,x)
  #print(out)
  if degrees == 45:
    order = fourtyfive(y,x,text)
  else:
    order = twentyfive(y,x,text)
  out = addition(out,order)
elif degrees == 135 or degrees == 315: #todo
  out = xyPY(y,x)
  if degrees == 135:
    order = thirtyfive(y,x,text)
  else:
    order = fifteen(y,x,text)
  out = addition(out,order)
elif degrees == 360 or degrees == 0:
  out = text
elif degrees == 180:
  for i in range(y-1,-1,-1): out.append(text[i][::-1])
elif degrees == 90:
  out = transpose(text)
  for i in range(x): out[i] = out[i][::-1]
elif degrees == 270:
  out = transpose(text)
  out.reverse()

for i in range (len(out)):
  out[i] = ''.join(out[i])
  print(out[i])

#print('\n'.join(out))