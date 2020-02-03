#https://open.kattis.com/problems/lostlineup
n = int(input())
output = ['1']
count = 0
positions = input().split(' ')
#print('positions:',positions)

for i in positions:
  output.append(str(positions.index(str(count)) + 2))
  count += 1
#print('out:',output)
print(' '.join(output))


