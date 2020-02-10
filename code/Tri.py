#https://open.kattis.com/problems/tri

num1,num2,num3 = input().split(' ')
num1 = int(num1)
num2 = int(num2)
num3 = int(num3)
#addition
if (num1+num2)==num3:
  print('%i+%i=%i'%(num1,num2,num3))
  quit()
if (num2+num3)==num1:
  print('%i=%i+%i'%(num1,num2,num3))
  quit()
#subtraction
if (num1-num2)==num3:
  print('%i-%i=%i'%(num1,num2,num3))
  quit()
if (num2-num3)==num1:
  print('%i=%i-%i'%(num1,num2,num3))
  quit()
#multiplicaiton
if (num1*num2)==num3:
  print('%i*%i=%i'%(num1,num2,num3))
  quit()
if (num2*num3)==num1:
  print('%i=%i*%i'%(num1,num2,num3))
  quit()
#division
if (num1/num2)==num3:
  print('%i/%i=%i'%(num1,num2,num3))
  quit()
if (num2/num3)==num1:
  print('%i=%i/%i'%(num1,num2,num3))
  quit()