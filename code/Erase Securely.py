#https://open.kattis.com/problems/erase

#delete level
n = int(input())
#more input
start = list(input())
end = list(input())
#debugging
print(start)
print(end)
#only need mod 2
n = n%2
# if n is 1 iterate once
if n == 1:
  #run through to change
  for i in range (0,len(start)):
    if start[i] == '0':
      start[i] = '1'
    elif start[i] == '1':
      start[i] = '0'
#debugging
print(''.join(start))
print(''.join(end))
#output
if start == end:
  print('Deletion succeeded')
else:
  print('Deletion failed')

