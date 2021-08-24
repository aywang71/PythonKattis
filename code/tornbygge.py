#https://open.kattis.com/problems/tornbygge

n = int(input())

b = input().split(' ')

count = 1

for num in range(1, len(b)):
  if int(b[num]) > int(b[num - 1]):
    count += 1
  
print(count)