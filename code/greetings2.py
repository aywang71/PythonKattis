#https://open.kattis.com/problems/greetings2

n = list(input())
out = ['h']

e = n.count('e') * 2

for i in range(e): out.append('e')

out.append('y')

print(''.join(out))