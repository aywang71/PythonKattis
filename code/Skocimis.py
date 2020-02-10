#https://open.kattis.com/problems/skocimis

#input and formatting
num1, num2, num3 = input().split(' ')
num1 = int(num1)
num2 = int(num2)
num3 = int(num3)
#if the space between the first two are larger or not
if (num2-num1-1) > (num3-num2-1):
  print(num2-num1-1)
else:
  print(num3-num2-1)