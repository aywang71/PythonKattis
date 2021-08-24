#https://open.kattis.com/problems/pauleigon

#input format
switch, num1 , num2 = input().split(' ')
switch = int(switch)
num1 = int(num1)
num2 = int(num2)
total = num1+num2
#number of times switched
rotations = total//switch
#debugging
print(rotations)
#if it divides its paul
if rotations%2 == 0:
  print('paul')
else:
  print('opponent')