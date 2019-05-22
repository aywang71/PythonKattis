#https://open.kattis.com/problems/nodup
#inputs string and split by spaces
n = input().split()
#DEBUGGING
print(n)
# counter variable
x = 0
#for loop to execute per list value
for i in range (0,len(n)):
  #sets counter value to a number larger than itself
  if x<n.count(n[i]):
    x = n.count(n[i])
  #if not, continue
  else:
    continue 
# if there are 2 or more occurences of the counter, print no
if x>=2:
  print('no')
else:
  print('yes')


