#https://open.kattis.com/problems/laptopsticker

s = input().split(' ')

for i in range(len(s)):
  s[i] = int(s[i])

if (s[0] -2) >= s[2] and (s[1] -2) >= s[3]:
  print(1)
else:
  print(0)