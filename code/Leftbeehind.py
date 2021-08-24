#https://open.kattis.com/problems/leftbeehind

#until 0 0
while True:
  #inputs
  good, bad =input().split(' ')
  good = int(good)
  bad = int(bad)
  if (good==0) and (bad==0):
    break
  #cases and output
  if (good+bad) == 13:
    print('Never speak again.')
  elif good > bad:
    print('To the convention.')
  elif bad > good:
    print('Left beehind.')
  elif bad == good:
    print('Undecided.')