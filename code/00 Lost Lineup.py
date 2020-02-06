#https://open.kattis.com/problems/lostlineup
n = int(input())
#output = ['1']
positions = input().split(' ')
#print('positions:',positions)

output = [str(positions.index(str(i)) + 2) for i in range (len(positions))]
output.insert('1',0)

#for i in range(0,len(positions)):
#  output.append(str(positions.index(str(i)) + 2))
#print('out:',output)
print(' '.join(output))