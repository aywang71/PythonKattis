#https://open.kattis.com/problems/owlandfox

#iteration
n = int(input())
for i in range (0,n):
  #number
  number = list(input())
  count = len(number)-1
  #calcuations
  while number[count] == '0':
    count -= 1
  number[count] = str(int(number[count])-1)
  #output
  if number.count('0') == len(number):
    print('0')
  else:
    print(''.join(number))
    
