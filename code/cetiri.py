#https://open.kattis.com/problems/cetiri

#input format
numbers = input().split(' ')
#integer conversion
for i in range (0,len(numbers)):
  numbers[i] = int(numbers[i])
numbers = sorted(numbers)
#debugging
print(numbers)
#if statement
if (numbers[1]-numbers[0]) == (numbers[2]-numbers[1]):
  print (numbers[2]+(numbers[1]-numbers[0]))
else:
  if numbers[1]-numbers[0]>numbers[2]-numbers[1]:
    larger = numbers[1]-numbers[0]
    point = 0
  else:
    larger = numbers[2]-numbers[1]
    point = 1
  #debugging
  print(larger,point)
  #output
  print(int(numbers[point]+(larger/2)))
