#https://open.kattis.com/problems/coconut

#need for levels
sequence = []
#input and format
s, p = input().split(' ')
s = int(s)
p = int(p)
#appends indexes to list
for i in range (1,p+1):
  x = str(2) +str(i)
  sequence.append(x)
#debugging
print(sequence)
#counts where to start
x = 0
while True:
  # goes until only one thing left
  if len(sequence) == 1:
    break
  #finds thing to eliminate
  elim_index = (x+s-1)%len(sequence)
  #does formatting to eliminate stuff
  elimination = list(sequence[elim_index])
  level = elimination[0]
  sequence.pop(elim_index)
  #debugging
  print('elimination index', elim_index)
  print('elimination',elimination)
  print('level:',level)
  #ifs, to specify formatting stuff
  if level == '2':
    insertable = str(1)+''.join(elimination)[1:]
    sequence.insert(elim_index,insertable)
    sequence.insert(elim_index,insertable)
    x = elim_index
  elif level == '1':
    insertable = str(0)+''.join(elimination)[1:]
    sequence.insert(elim_index,insertable)
    x = elim_index +1
  elif level == '0':
    x = elim_index
  #debugging
  print(sequence)
#prints index of the last one
final = sequence[0]
print(''.join(final[1:]))
