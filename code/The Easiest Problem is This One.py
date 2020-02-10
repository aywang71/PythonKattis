#https://open.kattis.com/problems/easiest

#looks for 0
while True:
  #input
  number =list(input())
  #data type formatting
  for i in range (0,len(number)):
    number[i] = int(number[i])
  #if its just 0, break
  if number[0] == 0:
    break
  original_sum = sum(number)
  #debugging
  print(original_sum)
  #starts multiplication number
  i = 11
  #data type formatting
  for x in range (0,len(number)):
    number[x] = str(number[x])
  #debugging
  print(number)
  #looks for correct i
  while True:
    #data type formatting
    new_number = list(str(int(''.join(number))*i))
    #debugging
    print(new_number)
    #data type formatting
    for x in range (0,len(new_number)):
      new_number[x] = int(new_number[x])
    #debugging
    print(new_number)
    #if and break
    if sum(new_number) == original_sum:
      print(i)
      break
    #runs back around
    i+= 1

    


  