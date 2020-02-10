#https://open.kattis.com/problems/luhnchecksum

#input
n = int(input())
for i in range (0,n):
  digits = list(input())
  for i in range (0,len(digits)):
    digits[i]  = int(digits[i])
  #sets up index in list
  i = 2
  #from end to beginning and case selection
  while i < (len(digits)+1):
    if digits[-i] <5:
      digits[-i] = digits[-i]*2
    elif digits[-i] == 5:
      digits[-i] = 1
    elif digits[-i] == 6:
      digits[-i] = 3
    elif digits[-i] == 7:
      digits[-i] = 5
    elif digits[-i] == 8:
      digits[-i] = 7
    elif digits[-i] == 9:
      digits[-i] = 9
    i += 2
  #debugging
  print(sum(digits))
  print(digits)
  #output
  if sum(digits)%10 == 0:
    print('PASS')
  else:
    print('FAIL')