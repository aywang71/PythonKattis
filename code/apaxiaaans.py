#https://open.kattis.com/problems/apaxiaaans

#proper input format
n = list(input())
#debugging portion
print(n)
print(len(n))
# For this range
for i in range (0,len(n)-1):
  # if the next one is equal to the current one, make the current one 0
  if n[i] == n[i+1]:
    n[i] = '0'
  else:
    continue
#debugging
print(n)
# for the amount of 0s in the list, remove them
for i in range (0,n.count('0')):
  n.remove('0')
# debugging
print(n)
#output format
print(''.join(n))
