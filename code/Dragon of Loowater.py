#https://open.kattis.com/problems/loowater

while True:
  dragon_l, knight_l = input().split(' ')
  dragon_l = int(dragon_l)
  knight_l = int(knight_l)
  dragon = []
  knight = []
  if (dragon_l == 0) and (knight_l == 0):
    break
  if knight_l < dragon_l:
    print('Loowater is doomed!')
    for i in range(dragon_l):
      dragon.append(int(input()))
    for i in range(knight_l):
      knight.append(int(input()))
    continue
  for i in range(dragon_l):
    dragon.append(int(input()))
  for i in range(knight_l):
    knight.append(int(input()))
  dragon.sort()
  knight.sort()
  #debug
  #print(dragon)
  #print(knight)
  gold = 0
  for i in knight:
    if len(dragon) == 0:
      break
    if i >= dragon[0]:
      #print(i, ' knight')
      gold += i
      dragon.pop(0)
  if len(dragon)>0:
    print('Loowater is doomed!')
  else:
    print(gold)
  #print('')