#input for amount of teams
n = int(input())
#storage values
universities = []
team_name = []
#asks for n inputs
for i in range (0,n):
  x =  input()
  y = x.split(' ')
  #only takes new inputs
  if y[0] in team_name:
    continue
  else:
    #appends uni to teamname and full to universities
    team_name.append(y[0])
    universities.append(y)
#debugging
print(team_name)
#debugging
print(universities)
#output format
if len(team_name)> 12:
  for i in range (0,12):
    print(' '.join(universities[i]))
else:
  for i in range (0,len(team_name)):
    print(' '.join(universities[i]))
