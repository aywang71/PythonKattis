#https://open.kattis.com/problems/stararrangements

#math function library
import math
#input
number = int(input())
#output formatting
print("%i:"%(number))
#only goes halfway to save processing time
for i in range (2,math.ceil(number/2)+1):
  #resets total
  total = 0
  #runs it for -1 intervals
  while total < number:
    total+= i
    #break
    if total == number:
      print("%i,%i"%(i,i-1))
      break
    total += i-1
    #break
    if total == number:
      print("%i,%i"%(i,i-1))
      break
  total = 0
  #check for the same rows
  if number%i == 0:
    print("%i,%i"%(i,i))

