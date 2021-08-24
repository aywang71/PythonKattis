#https://open.kattis.com/problems/musicalscales

#finds the scale for any start note
def find_scale(start):
  possible = [start]
  #sets up movement pattern
  move = [2,2,1,2,2,2,1]
  music = ['A','A#','B','C','C#','D','D#','E','F','F#','G','G#']
  x = music.index(start)
  for i in move:
    x  = (x+i)%12
    possible.append(music[x])
  #output
  return possible

#finds if the ntoes are present in given scale
def is_true(possible,notes):
  for i in notes:
    #uses boolean
    corr = False
    for x in possible:
      if i == x:
        corr = True
        break
      else:
        continue
    #return statement starts here
    if corr == False:
      return False
  return True

#removes any spaces which might be at the end
def remove_spaces(notes):
  count = 0
  while count < len(notes):
    if notes[count] == '':
      notes.pop(count)
    count += 1
  return notes
#sets up a chord
music_notes = ['A','A#','B','C','C#','D','D#','E','F','F#','G','G#']
# sets up input (n not used)
n = int(input())
notes = input().split(' ')
#removes spaces
remove_spaces(notes)
#this is our output list
output = []
#debugging
print(notes)
#run 12 times 
for i in range (0,12):
  #sets a list for possible note
  possible = find_scale(music_notes[i])
  #debugging
  print(music_notes[i])
  print(possible)
  #if everything is good
  if is_true(possible,notes):
    output.append(music_notes[i])
#output function
if len(output) == 0:
  print('none')
else:
  print(' '.join(output))
#debugging
print(output)