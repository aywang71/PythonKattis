#https://open.kattis.com/problems/prsteni

#input format
n = int(input())
ratios = input().split(' ')
for i in range (0,len(ratios)):
  ratios[i] = int(ratios[i])
  
#for everything after first term
for i in range (1,n):
  #assignment
  a,b = ratios[0], ratios[i]
  #check divisibility
  for j in range (1000,1,-1):
    if (a%j == 0) and (b%j == 0):
      a = a/j
      b = b/j
      break
  #output format
  print('%i/%i'%(a,b))
