#https://open.kattis.com/problems/basketballoneonone

#input format
x = input()
#makes vars for score coutning
a = 0
b = 0
# bool to check if count by 2 rule is active
by2 = False
#goes through at every second character
for i in range(0,len(x)-1,2):
  #adds the corresponding value to var a or b
  if x[i] == "A":
    a += int(x[i+1])
  elif x[i] =="B":
    b += int(x[i+1])
  #debugging
  else:
    print('read error')
  #if both scores reach 10 count by 2 rule is active
  if a == 10 and b == 10:
    by2 = True
  # runs the count by 2 rule
  if by2:
    if a >= (b + 2):
      print('A')
      break
    elif b >= (a + 2):
      print('B')
      break
  #regular output rules
  else:
    if a >= 11:
      print('A')
    elif b >= 11:
      print('B')
  #debugging
  print('A:',a)
  #debugging
  print('B:',b)
  #debugging
  print(by2)

  
