#https://open.kattis.com/problems/thegrandadventure

# makes a function to check and remove objects
def check(i,backpack):
  #if there is nothing in there then they auotmatically fail
  if len(backpack) == 0:
    return False, backpack
  if i == "b":
    if backpack[-1] == "$":
      backpack.pop()
      return True, backpack
  elif i == "j":
    if backpack[-1] == "*":
      backpack.pop()
      return True, backpack
  elif i == "t":
    if backpack[-1] == "|":
      backpack.pop()
      return True, backpack
  return False, backpack

# iteration input
for i in range(int(input())):
  #route
  n = list(input())
  backpack = []
  #temp bool for yes/no
  temp= True
  #runs through each character in the list 'n'
  for i in n:
    if i == '.':
      continue
    elif i == "$":
      backpack.append("$")
    elif i == "|":
      backpack.append("|")
    elif i == "*":
      backpack.append("*")
    elif i == "b":
      temp, backpack = check(i,backpack)
    elif i == "j":
      temp, backpack = check(i,backpack)
    elif i == "t":
      temp, backpack = check(i,backpack)
    if temp == False:
      print("NO")
      break
  #debugging
  print('list:',backpack,n)
  #final check and output
  if (temp == True) and len(backpack) == 0:
    print('YES')
  elif temp == True:
    print('NO')

    