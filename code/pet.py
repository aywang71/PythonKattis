#https://open.kattis.com/problems/pet
#input format
a = input().split()
b = input().split()
c = input().split()
d = input().split()
e = input().split()
#converts values to integer
for i in range (0,len(a)):
  a[i] = int(a[i])
for i in range (0,len(b)):
  b[i] = int(b[i])
for i in range (0,len(c)):
  c[i] = int(c[i])
for i in range (0,len(d)):
  d[i] = int(d[i])
for i in range (0,len(e)):
  e[i] = int(e[i])
#new storage values to sum a to e
f = sum(a)
g = sum(b)
h = sum(c)
i = sum(d)
j = sum(e)
l = []
#appends all of the storage values
l.append(f)
l.append(g)
l.append(h)
l.append(i)
l.append(j)
#output format
w = l.index(max(l))
w += 1
print (w,max(l))
