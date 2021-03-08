#https://open.kattis.com/problems/chopin

#sys for EOF
import sys
#dictionary for translations
translate = {
  'A# minor':'Bb minor',
  'A# major':'Bb major',
  'Bb minor':'A# minor',
  'Bb major':'A# major',

  'C# major':'Db major',
  'C# minor':'Db minor',
  'Db minor':'C# minor',
  'Db major':'C# major',

  'D# major':'Eb major',
  'D# minor':'Eb minor',
  'Eb major':'D# major',
  'Eb minor':'D# minor',

  'Ab minor':'G# minor',
  'Ab major':'G# major',
  'G# major':'Ab major',
  'G# minor':'Ab minor',

  'Gb minor':'F# minor',
  'Gb major':'F# major',
  'F# minor':'Gb minor',
  'F# major':'Gb major'
}
#count for output
count = 0
#reads EOF into list
notes = sys.stdin.read().split('\n')
notes.pop(-1)
#debugging
print(notes)
for note in notes:
  #debugging
  print(note)
  count += 1
  #translates note
  if note in translate :
    x = translate.get(note,'none')
    print('Case %i: %s'%(count,x))
  else:
    print('Case %i: UNIQUE'%(count))
#traditional input follows:
'''
n = int(input())
for i in range (n):
  note = input()
  count += 1
  if note in translate:
    x = translate.get(note,'none')
    print('Case %i: %s'%(count,x))
  else:
    print('Case %i: UNIQUE'%(count))

'''

  
