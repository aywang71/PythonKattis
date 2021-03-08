#https://open.kattis.com/problems/dasblinkenlights

#input
num1,num2,maxi = (int(x) for x in input().split(' '))
#finds lcm counter
x = max([num1,num2])
#counts for lcm
while True:
  if (x%num1 == 0) and (x%num2 == 0):
    break
  x +=1
#output
if x <=maxi:
  print('yes')
else:
  print('no')
