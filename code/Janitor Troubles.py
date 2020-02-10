#https://open.kattis.com/problems/janitortroubles

# for math.sqrt
import math
#input and split
a,b,c,d = input().split(' ')
a = int(a)
b = int(b)
c = int(c)
d = int(d)
#semi-perimeter
SP = (a+b+c+d)/2
#debugging
print(SP)
#brahmagupta's formula
area = math.sqrt((SP-a)*(SP-b)*(SP-c)*(SP-d))
#output format
print(area)