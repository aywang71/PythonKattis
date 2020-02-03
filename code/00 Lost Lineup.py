#https://open.kattis.com/problems/lostlineup
n = int(input())
output = [1]
count = 0
for i in range (n):
  positions = [int(i) for i in input().split(' ')]
print('positions:',positions)

for i in positions:
  temp = positions.index(count) + 1
  output.append(temp)
  count += 1

print(' '.join(output))


