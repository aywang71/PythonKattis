#https://open.kattis.com/problems/statistics

#to read EOF
import sys
#for output
count = 0

#until EOF
for line in sys.stdin:
  #for output, changes case number
  count += 1
  #formatting input
  numbers = line.split(' ')
  #convert to int
  for i in range (0,len(numbers)):
    numbers[i] = int(numbers[i])
  #1st number doesn't matter
  numbers.pop(0)
  #calculations
  mini = min(numbers)
  maxi = max(numbers)
  diff = maxi-mini
  #output
  print('Case %i: %i %i %i'%(count,mini,maxi,diff))
#traditional input
'''
number = int(input())
for i in range (0,number):
  count += 1
  numbers = input().split(' ')
  for i in range (0,len(numbers)):
    numbers[i] = int(numbers[i])
  numbers.pop(0)
  mini = min(numbers)
  maxi = max(numbers)
  diff = maxi-mini
  print('Case %i: %i %i %i'%(count,mini,maxi,diff))
'''