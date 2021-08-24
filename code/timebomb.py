#https://open.kattis.com/problems/timebomb

#copy for deepcopy
import copy
#for math.ceil
import math

#to check if 0
def is_zero(x):
  if (x[0][0] == '*') and (x[0][1] == '*') and (x[0][2] == '*') and (x[1][0] == '*') and (x[1][2] == '*') and (x[2][0] == '*') and (x[2][2] == '*') and (x[3][0] == '*') and (x[3][2] == '*') and (x[4][0] == '*') and (x[4][1] == '*') and (x[4][2] == '*') and (x[1][1] == ' ') and (x[2][1] == ' ') and (x[3][1] == ' '):
    return True
  else:
    return False

#to check if 1
def is_one(x):
  if (x[0][2] == '*') and (x[0][1] == ' ') and (x[0][0] == ' ') and (x[1][2] == '*') and (x[1][0] == ' ') and (x[1][1] == ' ') and (x[2][0] == ' ') and (x[2][1] == ' ') and (x[2][2] == '*') and (x[3][0] == ' ') and (x[3][1] == ' ') and (x[3][2] == '*') and (x[4][0] == ' ') and (x[4][1] == ' ') and (x[4][2] == '*'):
    return True
  else:
    return False

#to check if 2
def is_two(x):
  if (x[0][0] == '*') and (x[0][1] == '*') and (x[0][2] == '*') and (x[1][0] == ' ') and (x[1][1] == ' ') and (x[1][2] == '*') and (x[2][0] == '*') and (x[2][1] == '*') and (x[2][2] == '*') and (x[3][0] == '*') and (x[3][1] == ' ') and (x[3][2] == ' ') and (x[4][0] == '*') and (x[4][1] == '*') and (x[4][2] == '*'):
    return True
  else:
    return False

#to check if 3
def is_three(x):
  if (x[0][0] == '*') and (x[0][1] == '*') and (x[0][2] == '*') and (x[1][0] == ' ') and (x[1][1] == ' ') and (x[1][2] == '*') and (x[2][0] == '*') and (x[2][1] == '*') and (x[2][2] == '*') and (x[3][0] == ' ') and (x[3][1] == ' ') and (x[3][2] == '*') and (x[4][0] == '*') and (x[4][1] == '*') and (x[4][2] == '*'):
    return True
  else:
    return False

#to check if 4
def is_four(x):
  if (x[0][0] == '*') and (x[0][1] == ' ') and (x[0][2] == '*') and (x[1][0] == '*') and (x[1][1] == ' ') and (x[1][2] == '*') and (x[2][0] == '*') and (x[2][1] == '*') and (x[2][2] == '*') and (x[3][1] == ' ') and (x[3][0] == ' ') and (x[3][2] == '*') and (x[4][0] == ' ') and (x[4][1] == ' ') and (x[4][2] == '*'):
    return True
  else:
    return False

#to check if 5
def is_five(x):
  if (x[0][0] == '*') and (x[0][1] == '*') and (x[0][2] == '*') and (x[1][0] == '*') and (x[1][1] == ' ') and (x[1][2] == ' ') and (x[2][0] == '*') and (x[2][1] == '*') and (x[2][2] == '*') and (x[3][0] == ' ') and (x[3][1] == ' ') and (x[3][2] == '*') and (x[4][0] == '*') and (x[4][1] == '*') and (x[4][2] == '*'):
    return True
  else:
    return False

#to check if 6
def is_six(x):
  if (x[0][0] == '*') and (x[0][1] == '*') and (x[0][2] == '*') and (x[1][0] == '*') and (x[1][1] == ' ') and (x[1][2] == ' ') and (x[2][0] == '*') and (x[2][1] == '*') and (x[2][2] == '*') and (x[3][0] == '*') and (x[3][1] == ' ') and (x[3][2] == '*') and (x[4][0] == '*') and (x[4][1] == '*') and (x[4][2] == '*'):
    return True
  else:
    return False

#to check if 7
def is_seven(x):
  if (x[0][0] == '*') and (x[0][1] == '*') and (x[0][2] == '*') and (x[1][0] == ' ') and (x[1][1] == ' ') and (x[1][2] == '*') and (x[2][0] == ' ') and (x[2][1] == ' ') and (x[2][2] == '*') and (x[3][0] == ' ') and (x[3][1] == ' ') and (x[3][2] == '*') and (x[4][0] == ' ') and (x[4][1] == ' ') and (x[4][2] == '*'):
    return True
  else:
    return False

#to check if 8
def is_eight(x):
  if (x[0][0] == '*') and (x[0][1] == '*') and (x[0][2] == '*') and (x[1][0] == '*') and (x[1][1] == ' ') and (x[1][2] == '*') and (x[2][0] == '*') and (x[2][1] == '*') and (x[2][2] == '*') and (x[3][0] == '*') and (x[3][1] == ' ') and (x[3][2] == '*') and (x[4][0] == '*') and (x[4][1] == '*') and (x[4][2] == '*'):
    return True
  else:
    return False

#to check if 9
def is_nine(x):
  if (x[0][0] == '*') and (x[0][1] == '*') and (x[0][2] == '*') and (x[1][0] == '*') and (x[1][1] == ' ') and (x[1][2] == '*') and (x[2][0] == '*') and (x[2][1] == '*') and (x[2][2] == '*') and (x[3][0] == ' ') and (x[3][1] == ' ') and (x[3][2] == '*') and (x[4][0] == '*') and (x[4][1] == '*') and (x[4][2] == '*'):
    return True
  else:
    return False

#finds a number
def find_num(temp):
  if is_one(temp) == True:
    return 1
  elif is_two(temp) == True:
    return 2
  elif is_three(temp) == True:
    return 3
  elif is_four(temp) == True:
    return 4
  elif is_five(temp) == True:
    return 5
  elif is_six(temp) == True:
    return 6
  elif is_seven(temp) == True:
    return 7
  elif is_eight(temp) == True:
    return 8
  elif is_nine(temp) == True:
    return 9
  elif is_zero(temp) == True:
    return 0
  else:
    return -200

#formats number in correct way
def get_num(whole):
  temp_list = []
  #print(whole)
  for x in range (0,len(whole)):
    i = list(whole[x])
    temp_temp = [i[0],i[1],i[2]]
    temp_list.append(copy.deepcopy(temp_temp))
    i = list(i)
    i.pop(0)
    i.pop(0)
    i.pop(0)
    try:
      i.pop(0)
    except:
      pass
    whole[x] = ''.join(i)
  return temp_list, whole

#common input and presetting
number =[]
whole = []
for i in range (0,5):
  line = input()
  length = len(line)
  whole.append(line)
#debugging
print(whole)

#runs functions through length of string
for i in range (0,math.ceil(length/4)):
  temp,whole = get_num(whole)
  #debugging
  for i in temp:
    print(''.join(i))
    #appends as string to join later
  number.append(str(find_num(temp)))
  #debugging
  print('our number is:',find_num(temp))
#debugging
print(number)
#output
if '-200' in number:
  print('BOOM!!')
elif (int(''.join(number))%6) == 0:
  print('BEER!!')
else:
  print('BOOM!!')