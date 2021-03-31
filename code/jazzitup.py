#https://open.kattis.com/problems/jazzitup

#essentially you are just looking for the first coprime
n = int(input())

for i in range (2, n):
  #print('iteration:', i)
  if n % i == 0: 
    #print('is a factor')
    continue
  #check that none of the factors of i are divisible in n:
  passed = True
  for x in range (2,i):
    if i % x == 0 and n % x == 0: 
      #print('is not coprime)')
      passed = False
      break
  if passed: 
    print(i)
    break
