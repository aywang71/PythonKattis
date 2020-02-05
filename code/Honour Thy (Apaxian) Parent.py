#https://open.kattis.com/problems/apaxianparent

#input format
names = input().split(' ')

#output rules
if names[0][-1] == 'e':
  #debugging
  print(1)
  print(''.join([names[0],'x',names[1]]))
elif names[0][-2::] == 'ex':
  #debugging
  print(2)
  print(''.join(names))
elif names[0][-1] in ['a','i','o','u']:
  #debugging
  print(3)
  print(''.join([names[0][0:-1],'ex',names[1]]))
else:
  #debugging
  print(4)
  print(''.join([names[0],'ex',names[1]]))