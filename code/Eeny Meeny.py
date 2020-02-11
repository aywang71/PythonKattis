#https://open.kattis.com/problems/eenymeeny

#starts a counter variable
counter = len(input().split(' '))
#makes storage, output, and bool switch
names = []
team1 = []
team2 = []
switch = True

#more input for n 
for i in range (int(input())):
  names.append(input())
#debugging
print('names',names)
#variable to mod
temp_count = 0

#until we use all the names
while len(names) != 0:
  #updates temp_count and simulates circular motion
  temp_count = (temp_count+counter-1)%len(names) 
  #debuggin
  print('temp_count:',temp_count)
  #adds name to either team1 or team2
  if switch:
    team1.append(names[temp_count])
    names.remove(names[temp_count])
    switch = False
  else:
    team2.append(names[temp_count])
    names.remove(names[temp_count])
    switch = True
  #debugging
  print('names',names)
  print('team 1:',team1)
  print('team 2:',team2)

#output
print(len(team1))
for i in team1:
  print(i)
print(len(team2))
for i in team2:
  print(i)
