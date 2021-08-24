#https://open.kattis.com/problems/sumkindofproblem

#input for iterations
n= int(input())
for i in range (0,n):
  #input for test number and amount of digits
  test,digits = input().split(' ')
  test = int(test)
  digits = int(digits)
  #formulas
  s1 = (1+digits)*digits/2
  s2 = (2+digits*2)*digits/2
  s3 = (1+digits*2-1)*digits/2
  #outputs
  print("%i %i %i %i" %(test,s1,s3,s2))
