#https://open.kattis.com/problems/bubbletea

#line 1 input
tea = int(input())

#line 2 input
teas = input().split(' ')
for i in range (0,len(teas)):
  teas[i] = int(teas[i])

#line 3 input
topping = int(input())

#line 4 input
toppings = input().split(' ')
for i in range (0,len(toppings)):
  toppings[i] = int(toppings[i])

#line 5 input
restrictions = []
for i in range (0,tea):
  x = input().split(' ')
  x.pop(0)
  for i in range (0,len(x)):
    x[i] = int(x[i]) - 1
  restrictions.append(x)

#debugging
print('toppings:',toppings)
#bigger than max
mini = 10 ** 10
#debugging
print('restrictions:',restrictions)
#nested for loop 
for i in range (0,len(teas)):
  allowed = restrictions[i]
  #debugging
  print('allowed:',allowed)
  for x in range (0,len(toppings)):
    if x in allowed:
      #debugging
      print('in:',x)
      print('cost:',teas[i]+toppings[x])
      #resets mini
      if (teas[i] + toppings[x]) < mini:
        mini = teas[i] + toppings[x]
#line 6 input
budget = int(input())
#debugging
print('mini:',mini)
#output format
if mini > budget:
  print(0)
else:
  print((budget//mini)-1)
