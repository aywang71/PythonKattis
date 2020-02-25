#https://open.kattis.com/problems/yoda

#inputs and declares outputs
num1 = list(input())
num1new = []
num2 = list(input())
num2new = []
#if length equal, then go and compare
if len(num1) == len(num2):
  for i in range (len(num1)):
    if int(num1[i]) > int(num2[i]):
      num1new.append(num1[i])
    elif int(num2[i]) > int(num1[i]):
      num2new.append(num2[i])
    else:
      num1new.append(num1[i])
      num2new.append(num2[i])
else:
  #finds the shorter
  mini = min([len(num1),len(num2)])
  #debugging
  print(mini)
  #if statement to find the shorter one
  if mini == len(num1):
    #goes throught the beginning of the longer one and adds to output list
    for i in range ((len(num2)-mini)):
      num2new.append(num2[0])
      num2.pop(0)
    #debugging
    print(num2)
    #same code because now the lists are equal length
    for i in range (len(num1)):
      if int(num1[i]) > int(num2[i]):
        num1new.append(num1[i])
      elif int(num2[i]) > int(num1[i]):
        num2new.append(num2[i])
      else:
        num1new.append(num1[i])
        num2new.append(num2[i])
  #see above commenting
  else:
    for i in range ((len(num1)-mini)):
      num1new.append(num1[0])
      num1.pop(0)
    #debugging
    print(num1)
    for i in range (len(num1)):
      if int(num1[i]) > int(num2[i]):
        num1new.append(num1[i])
      elif int(num2[i]) > int(num1[i]):
        num2new.append(num2[i])
      else:
        num1new.append(num1[i])
        num2new.append(num2[i])
#output
if len(num1new) == 0:
  print('YODA')
else:
  print(int(''.join(num1new)))
if len(num2new) == 0:
  print('YODA')
else:
  print(int(''.join(num2new)))
