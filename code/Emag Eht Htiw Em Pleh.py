#https://open.kattis.com/problems/empleh

#prints the between thing
between = '+---+---+---+---+---+---+---+---+'
#input
try:
  white2 = input().split()
  white2 = white2[1].split(',')
except:
  white2 = []
try:
  black2 = input().split()
  black2 = black2[1].split(',')
except:
    black2 = []
#used to match the letter to a cell reference
conversion = ['a','b','c','d','e','f','g','h']
#goes through to match the cell to a nested list
white = [[],[],[],[],[],[],[],[]]
black = [[],[],[],[],[],[],[],[]]
for i in white2:
  white[int(i[-1])-1].append(i)
for i in black2:
  black[int(i[-1])-1].append(i)
#debugging
print('white:',white)
print('black:',black)

#first between, for the top margin
print(between)
#goes throughh list backwards 
for i in range (8,0,-1):
  #debugging
  print('i:',i)
  # alternates rows
  if i%2 == 0:
    row = list('|...|:::|...|:::|...|:::|...|:::|')
  else:
    row = list('|:::|...|:::|...|:::|...|:::|...|')
  #temporary list in nested list
  white_temp = white[i-1]
  black_temp = black[i-1]
  #updates row
  for x in white_temp:
    if len(x) == 3:
        row[conversion.index(x[-2])*4+2] = x[0].upper()
    else:
        row[conversion.index(x[-2])*4+2] = 'P'
  for x in black_temp:
    if len(x) == 3:
        row[conversion.index(x[-2])*4+2] = x[0].lower()
    else:
        row[conversion.index(x[-2])*4+2] = 'p'
  #output format
  print(''.join(row))
  print(between)

      