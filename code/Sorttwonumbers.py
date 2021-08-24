#https://open.kattis.com/problems/sorttwonumbers

n = input().split(' ')

for i in range(len(n)): n[i] = int(n[i])

n = sorted(n)

for i in range(len(n)): n[i] = str(n[i])

print(' '.join(n))