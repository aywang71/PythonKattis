#https://open.kattis.com/problems/numberfun

#iteration inputs
n= int(input())
for i in range (0,n):
  #numeric input
  num1,num2,total = input().split(' ')
  num1 = int(num1)
  num2 = int(num2)
  total = int(total)
  #tests
  if num1+num2 == total:
    print('Possible')
    continue
  elif num1*num2 == total:
    print('Possible')
    continue
  elif num1/num2 == total:
    print('Possible')
    continue
  elif num2/num1 == total:
    print('Possible')
    continue
  elif num1-num2 == total:
    print('Possible')
    continue
  elif num2-num1 == total:
    print('Possible')
    continue
  print('Impossible')