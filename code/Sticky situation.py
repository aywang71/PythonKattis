#https://open.kattis.com/problems/stickysituation

#range input
x = int(input())
#boolean to run through for loop
output = False
#makes a list of sticks with integers
sticks = [int(i) for i in input().split(' ')]
#sorts lowest to highest
sticks.sort()
#goes through input range
for i in range(0, x):
  # if counter is within 3 of max 
  if i + 2 >= x:
    break
  #if the current stick + next stick is greater than the 3rd stick
  if (sticks[i] + sticks[i+1] > sticks[i+2]):
    output = True
#if output is true
if output:
  print('possible')
else:
  print('impossible')