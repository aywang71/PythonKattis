#https://open.kattis.com/problems/falsesecurity

#sys for getting inputs
import sys
#lists for alphabet and moresecode
alphabet = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ_,.?')
morsecode = ['.-','-...','-.-.','-..','.','..-.','--.','....','..','.---','-.-','.-..','--','-.','---','.--.','--.-','.-.','...','-','..-','...-','.--','-..-','-.--','--..','..--','.-.-','---.','----']
#input as one large string block
coded = []
numbers= []
morse = []
#gets inputs
for line in sys.stdin:
  var = list(line.strip())
  coded.append(var)
#alternate manual input
'''
while True:
  line = list(input())
  if '0' in line:
    break
  coded.append(line)
'''
#deubugging
print(coded)
print(len(coded))
#convert each line to morse code
for i in range (0,len(coded)):
  #replace letter with morse code equlivilant and append integer to end 
  num_list = []
  char_list =[]
  for x in range (0,len(coded[i])):
    char = morsecode[alphabet.index(coded[i][x])]
    #debugging
    print(char)
    #appends numbers and character 
    char_list.append(char)
    num_list.append(str(len(char)))
  #make a new integer with the lengths of each character
  #reverse integer
  #debugging
  print(''.join(num_list))
  print(''.join(char_list))
  #reverses numbers and joins characters
  num_list.reverse()
  char_list = ''.join(char_list)
  #decode morse code line
  sentence = []
  count = 0
  previous = 0
  #re-does morse and character values
  for i in range (0,len(num_list)):
    count += int(num_list[i])
    character = alphabet[morsecode.index(char_list[previous:count])]
    #debugging
    print(character)
    #resets for next ieration and appends
    sentence.append(character)
    previous = count
  #output format
  print(''.join(sentence))


    
