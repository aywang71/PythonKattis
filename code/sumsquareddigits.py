#https://open.kattis.com/problems/sumsquareddigits

#number of iterations
n = int(input())
for i in range (0,n):
  #more inputs
  iteration, base, number = input().split(' ')
  base = int(base)
  number = int(number)
  #finds largest digit
  x = 0
  while base ** x <= number:
    x+= 1
  #resets base value list
  base_value = []
  #goes down from largest value to find it
  for i in range (x-1,-1,-1):
    coefficent = number//(base**i)
    base_value.append(coefficent)
    number -= coefficent * (base**i)
  #debugging
  print(base_value)
  #makes each value squared
  for i in range (0,len(base_value)):
    base_value[i] = base_value[i] *base_value[i]
  #debugging
  print(base_value)
  #sum
  total = sum(base_value)
  #output
  print('%s %i' %(iteration,total))
    

