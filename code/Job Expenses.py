#https://open.kattis.com/problems/jobexpenses

#input
n = int(input())
#if input 0
if n == 0:
  print(0)
else:
  #more input
  money = input().split(' ')
  print(abs(sum(int(i) for i in money if int(i) < 0)))
    

