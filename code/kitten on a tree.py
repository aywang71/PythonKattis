#https://open.kattis.com/problems/kitten

#input for beginning position
start = int(input())
#path which is taken, also output
path = [str(start)]
branches = []
placehold = False

#goes through to find the "current" in question
def find (branches,current,path):
  for i in branches:
    if current in i[1:]:
      path.append(str(i[0]))
      current = i[0]
      return current,path,False
  return current,path,True

#until input is '-1'
while True:
  #more input
  branch = input().split(' ')
  if branch[0] == '-1':
    break
  elif branch[0] == str(start):
    continue
  #conversion to integer
  for i in range (0,len(branch)):
    branch[i] = int(branch[i])
  branches.append(branch)
#debugging
print(branches)
#until they have reached the end
while placehold == False:
  start,path,placehold = find(branches,start,path)
  #debugging
  print('current:',start)
  print('path:',path)
print('path:',path)
#output
print(' '.join(path))