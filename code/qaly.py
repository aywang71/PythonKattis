#https://open.kattis.com/problems/qaly
n = int(input())
sum = float(0)
for i in range (0,n):
  a,b = input().split()
  a = float(a)
  b = float(b)
  sum = sum + (a*b)

print(sum)
