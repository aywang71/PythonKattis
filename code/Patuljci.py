#https://open.kattis.com/problems/patuljci

#store inputs
numbers = []
#input
for i in range (0,9):
  x = int(input())
  numbers.append(x)
#iteration boolean
stop = False
#loop twice for two extra dwarves
for i in range (0,len(numbers)):
  for x in range (0,len(numbers)):
    #each number is unique
    if numbers[i] == numbers[x]:
      continue
    #checks if removing those two makes it 100
    if (sum(numbers)-numbers[i]-numbers[x]) == 100:
      #debugging
      print(numbers[i],i,numbers[x],x,(sum(numbers)-numbers[i]-numbers[x]))
      #removes those unneeded numbers
      numbers.remove(numbers[x])
      #debugging
      print(numbers)
      numbers.remove(numbers[i])
      #debugging
      print(numbers)
      #to break outer loop
      stop = True
      break
  #used here to break again
  if stop == True:
    break
#output format
for i in range (0,len(numbers)):
  print(numbers[i])