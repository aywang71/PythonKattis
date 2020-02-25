#https://open.kattis.com/problems/bookingaroom

#input format
rooms, n = input().split(' ')
#occupied rooms
taken = []
#inputs and assigns to taken
for i in range (0,int(n)):
  room = int(input())
  taken.append(room)
#to output finished
boo = False
#runs through taken list
for i in range (1,int(rooms)+1):
  if i in taken:
    continue
  else:
    #portion of output
    boo = True
    print(i)
    break
#finish output
if boo == False:
  print('too late')