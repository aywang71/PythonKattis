#finds the x,y coordinates of a inserted list
def match (keyboard,string):
  output = []
  for i in string:
    for j in range(len(keyboard)):
      if i in keyboard[j]:
        #appends to output a pair of coordinates, x and y
        output.append([keyboard[j].index(i)+1,j+1])
        #debugging
        print('output:',output)
        break
  #gives out output
  return output
#comparision as a base for x,y coordinates
keyboard = ['qwertyuiop',
'asdfghjkl',Ta
'zxcvbnm']
#iteration input
n = int(input())
for i in range (n):
  #inputs the root of comparision and occurances
  root, occur = input().split(' ')
  root = match(keyboard,root)
  #debugging
  print('root:',root)
  #output
  out = []
  for x in range (int(occur)):
    #resets total count
    tot = 0
    #case of input
    case = input()
    #makes an x,y coordinate list
    compare = match(keyboard,case)
    #debugging
    print('input:',compare)
    #goes through the input to add on to total 
    for j in range(len(compare)):
      tot += abs(compare[j][0] - root[j][0]) + abs(compare[j][1]-root[j][1])
    #output format is a sublist consisting of a case and total
    out.append([case,tot])
  #sorts output
  out.sort(key = lambda x: (x[1],x[0]))
  #output
  for i in out:
    print(i[0],i[1])
  
          
