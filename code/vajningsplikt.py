#https://open.kattis.com/problems/vajningsplikt

arrive, leave, other = input().split(' ')

directions = ['North', 'East', 'South', 'West']

def check (arrive, leave, other):
  #checking that you're going across
  if leave == directions[(directions.index(arrive) + 2) % 4]:
    if other == directions[(directions.index(arrive) - 1) % 4]: 
      return 'Yes'
  #checking if it is a left turn
  if leave == directions[(directions.index(arrive) + 1) % 4]:
    if other == directions[(directions.index(arrive) + 2) % 4]: 
      #print('condition 2')
      return 'Yes'
    if other == directions[(directions.index(arrive) - 1) % 4]:
      #print('condition 3')
      return 'Yes'
  return 'No'

print(check(arrive,leave,other))