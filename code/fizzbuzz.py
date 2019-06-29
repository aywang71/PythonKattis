#https://open.kattis.com/problems/fizzbuzz
#input format
x,y,n = input().split(' ')
#converts to integer
x = int(x)
y = int(y)
n = int(n)
#output format
for i in range (1,n+1):
  if i%x == 0 and i%y == 0:
    print('FizzBuzz')
  elif i%x == 0:
    print('Fizz')
  elif i%y == 0:
    print('Buzz')
  else:
    print(i)
