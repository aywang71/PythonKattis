#https://open.kattis.com/problems/nop
string = list(input())
string.pop(0)
count = 1
addBlanks = 0

for i in string: 
  #print('letter', i)
  if i.isupper() and (count % 4 != 0):
    #print('changed', addBlanks)
    addBlanks += 4-(count % 4) 
    count = 1
  elif i.isupper() and (count % 4 == 0):
    #print('good')
    count = 1
  else:
    #print('lowercase')
    count += 1

print(addBlanks)