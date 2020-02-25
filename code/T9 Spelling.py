#https://open.kattis.com/problems/t9spelling

#inset list for better index and number tracking 
alphabet = [['a','b','c'],['d','e','f'],['g','h','i'],['j','k','l'],['m','n','o'],['p','q','r','s'],['t','u','v'],['w','x','y','z'],[' ']]

#finds the numberic format for the letter
def find (letter,alphabet):
  for i in range (0,len(alphabet)):
    if letter in alphabet[i]:
      x = i + 2
      y = alphabet[i]
      break
  if x==10:
    x = 0
  elif y.index(letter) == 0:
    x = x * 1
  elif y.index(letter) == 1:
    x = x * 11
  elif y.index(letter) == 2:
    x = x * 111
  elif y.index(letter) == 3:
    x = x * 1111
  #debugging
  print(x)
  return str(x)

#adds spaces where needed
def debug (converted):
  #uses while, because spaces are inserted
  i = 1
  while i < len(converted):
    #starts a one so we can look backwards
    x = converted[i]
    y = converted[i-1]
    if x[0] == y[0]:
      #insertion
      converted.insert(i,' ')
    i += 1
  return converted

#iteration input
n = int(input())
for i in range (0,n):
  #word input
  convert = list(input())
  converted = []
  for x in range (0,len(convert)):
    #finds each letter
    index = find(convert[x],alphabet)
    converted.append(index)
  #debugging
  print(converted)
  converted = debug(converted)
  #output format
  print('Case #%i:'%(i+1),''.join(converted))
  
