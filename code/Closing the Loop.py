#https://open.kattis.com/problems/closingtheloop

#iteration input
n = int(input())
for z in range (1,n+1):
  #inputs for rope lengths
  rope = int(input())
  #lists for future storage
  blue = []
  red = []
  total = []
  ropes = input().split(' ')
  if rope == 1:
    print('Case #%i: 0'%(z))
    continue
  #debugging
  print(ropes)
  #appends to seperate red/blue lists
  for i in ropes:
    if i[-1] == "R":
      red.append(int(i[:-1]))
    else:
      blue.append(int(i[:-1]))
  #sorts by order
  red.sort(reverse=True)
  blue.sort(reverse=True)
  #debugging
  print('red',red)
  print('blue',blue)
  #if/elif/else to check iterations and total 
  if len(red)> len(blue):
    #debugging
    print('blue less')
    #appends values
    for i in range (0,len(blue)):
      total.append(blue[i])
      total.append(red[i])
      total.append(-2)
  elif len(blue)>len(red):
    #debugging
    print('red less')
    #appends values
    for i in range (0,len(red)):
      total.append(blue[i])
      total.append(red[i])
      total.append(-2)
  else:
    #debugging
    print('equal')
    #appends values
    for i in range (0,len(blue)):
      total.append(blue[i])
      total.append(red[i])
      total.append(-2)
  #debugging
  print(total)
  #output formatting
  print('Case #%i: %i'%(z,sum(total)))
