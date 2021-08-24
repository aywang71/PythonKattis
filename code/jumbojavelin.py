#https://open.kattis.com/problems/jumbojavelin

n = int(input())
j = []

for i in range(n):
  j.append(int(input()))

print(sum(j) - len(j) + 1)
