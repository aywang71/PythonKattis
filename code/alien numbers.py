#https://open.kattis.com/problems/aliennumbers

#function to convert to base 10 - number is in the original base, source is the base used for conversion
def to_10 (num,source):
  #converting num from an unknown base
  number = list(num)
  #reverse num to make it easier to calculate
  number = number[::-1]
  #debugging
  #print('num:',number)
  #turns the source into a list to retrieve relative indexes
  source = list(source)
  #debugging
  #print('source:',source)
  #i represents the digit place
  for i in range(len(number)):
    number[i] = source.index(number[i]) * (len(source)**i)
  #debugging
  #print('number in base 10:',number)
  return sum(number)

# function to find the maximum number of digits when converting from base 10 to an unknown base
def large (num,base_num):
  # where n is the number of digits
  n = 0
  # while loop to find the first n to exceed num
  while (base_num ** n) <= num:
    #print('runthrough',n)
    n += 1
  #takes one away to find the right number of digits - we know where to start for 'from_10'
  n -= 1
  #debugging
  #print('number of digits:', n)
  return n

# function to convert from base 10 to a certain given base
def from_10 (num,source):
  #we know num is in base 10
  output = []
  source = list(source)
  #base is the base number (i.e base 2, 3,etc)
  base = len(source)
  #print('Base number',base)
  #runs 'large' function to find the number of digits when the base 10 number is converted to our base n - we know how large to start calculations at
  n = large(num,base)
  number = num
  while n >= 0:
    #the value is going to be the digit value of the output
    value = number//(base**n)
    number -= value * (base**n)
    #print('value:',value)
    #appens to output the corresponding character of our value in the ba
    output.append(source[value])
    #print('output currently:', output)
    #moves the digit value down once)
    n -=1
  return ''.join(output)

x = int(input())
for i in range (x):
  inputs = input().split(' ')
  #debugging
  #print(inputs)
  num = inputs[0]
  source = inputs[1]
  out = inputs[2]
  #now the input number has been converted from source base to base 10
  num = to_10(num,source)
  #debugging
  #print('Number in base 10:',num)
  print('Case #%s:' % (i+1),from_10(num,out))