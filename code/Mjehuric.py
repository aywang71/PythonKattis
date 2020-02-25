#https://open.kattis.com/problems/mjehuric

#checks for each value being 1 2 3 4 or 5
def check(sequence):
  if sequence[0] == 1:
    pass
  else:
    return False
  if sequence[1] == 2:
    pass
  else:
    return False
  if sequence[2] == 3:
    pass
  else:
    return False
  if sequence[3] == 4:
    pass
  else:
    return False
  if sequence[4] == 5:
    pass
  else:
    return False
  return True

#converts to string
def convertstr(sequence):
  for i in range (0,len(sequence)):
    sequence[i] = str(sequence[i])
  return sequence
#converts to integer
def convertint(sequence):
  for i in range (0,len(sequence)):
    sequence[i] = int(sequence[i])
  return sequence

#runs through sequence to switch values
def change (sequence):
  if sequence[0] > sequence[1]:
    x = sequence[0]
    sequence[0] = sequence[1]
    sequence[1] = x
    convertstr(sequence)
    print(' '.join(sequence))
    convertint(sequence)
  if sequence[1] > sequence[2]:
    x = sequence[1]
    sequence[1] = sequence[2]
    sequence[2] = x
    convertstr(sequence)
    print(' '.join(sequence))
    convertint(sequence)
  if sequence[2] > sequence[3]:
    x = sequence[2]
    sequence[2] = sequence[3]
    sequence[3] = x
    convertstr(sequence)
    print(' '.join(sequence))
    convertint(sequence)
  if sequence[3] > sequence[4]:
    x = sequence[3]
    sequence[3] = sequence[4]
    sequence[4] = x
    convertstr(sequence)
    print(' '.join(sequence))
  return sequence

#input format
sequence = input().split(' ')
#conversion
convertint(sequence)
#until done
while True:
  change(sequence)
  if check(sequence):
    break
  convertint(sequence)
  
