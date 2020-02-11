#https://open.kattis.com/problems/lineup

#iteration input
n = int(input())
names = []
#gets inputs
for i in range (0,n):
  name = input()
  names.append(name)
#checks for max/min
if max(names) == names[0] and min(names) == names[-1]:
  #checks until one left
  while True:
    if len(names) == 1:
      print('DECREASING')
      break
    elif max(names) == names[0]:
      names.pop(0)
    else:
      print('NEITHER')
      break
# if it goes increasing
elif max(names) == names[-1] and min(names) == names[0]:
  #checks until one left
  while True:
    if len(names) == 1:
      print('INCREASING')
      break
    elif min(names) == names[0]:
      names.pop(0)
    else:
      print('NEITHER')
      break
else:
  print('NEITHER')