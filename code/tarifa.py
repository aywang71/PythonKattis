#https://open.kattis.com/problems/tarifa
#input format
a = int(input())
n = int(input())
#storage values
b = a
i = 1
c = 0
# n times, to see the leftover data
while i <=n:
  i += 1
  x = int(input())
  b = a
  b = a-x
  c = c+b
c = c + a
#output format
print(c)

