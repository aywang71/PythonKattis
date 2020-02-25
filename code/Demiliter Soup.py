#https://open.kattis.com/problems/delimitersoup

#function to find parenthesis next to each other disregarding ' '
def findpar(demiliter):
  for i in range (0,len(demiliter)):
    if demiliter[i] == '(':
      for j in range (i+1,len(demiliter)):
        if demiliter[j] == ' ':
          continue
        elif demiliter[j] == ')':
          demiliter[i] = ' '
          demiliter[j] = ' '
          return demiliter, True
        break
  return demiliter, False
#function to find brackets next to each other disregarding ' '
def findcur(demiliter):
  for i in range (0,len(demiliter)):
    if demiliter[i] == '{':
      for j in range (i+1,len(demiliter)):
        if demiliter[j] == ' ':
          continue
        elif demiliter[j] == '}':
          demiliter[i] = ' '
          demiliter[j] = ' '
          return demiliter, True
        break
  return demiliter, False
#function to find curley next to each other disregarding ' '
def findbar(demiliter):
  for i in range (0,len(demiliter)):
    if demiliter[i] == '[':
      for j in range (i+1,len(demiliter)):
        if demiliter[j] == ' ':
          continue
        elif demiliter[j] == ']':
          demiliter[i] = ' '
          demiliter[j] = ' '
          return demiliter, True
        break
  return demiliter, False

#input
n = int(input())
demiliter = list(input())
#runs finding functions until  nothing left
while len(demiliter)>1:
  x, y, z = False, False, False
  demiliter, x = findpar(demiliter)
  if x:
    #debugging
    print(''.join(demiliter))
    continue
  demiliter, y = findcur(demiliter)
  if y:
    continue
    #debugging
    print(''.join(demiliter))
  demiliter, z = findbar(demiliter)
  if z:
    continue
    #debugging
    print(''.join(demiliter))
  break
#debugging
print('done',demiliter)


output = [500,500,500]
bad = False
#gest indexes
if (')' in demiliter):
  bad = True
  output[0] = (demiliter.index(')'))
if (']' in demiliter):
  bad = True
  output[1] = (demiliter.index(']'))
if ('}' in demiliter):
  bad = True
  output[2] = (demiliter.index('}'))
#debugging
print(output)
#uses boolean system 
if bad == False:
  print('ok so far')
else:
  # runs for negative output
  mini = min(output)
  if mini == output[0]:
    print(')',mini)
  elif mini == output[1]:
    print(']',mini)
  elif mini == output[2]:
    print('}',mini)