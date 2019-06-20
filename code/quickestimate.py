#https://open.kattis.com/problems/quickestimate
#input format
n= int(input())
#storage of digits
digits =[]
#n amount of numbers input
for i in range (0,n):
  #takes cost input into list, then append length to digits
  cost = list(input())
  digits.append(len(cost))
#ouput format
for i in range (0,len(digits)):
  print(digits[i])
