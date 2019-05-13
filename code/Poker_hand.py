#https://open.kattis.com/problems/pokerhand
n = input().split()
a = []
l =[]
counter = 0
#This is a loop to find the first character of each array value
for w in n:
  a.append(w[0])
for i in range (2,10):
  str_i = str(i)
  l.append(a.count(str_i))
l.append(a.count("A"))
l.append(a.count("J"))
l.append(a.count("Q"))
l.append(a.count("K"))
l.append(a.count("T"))
counter = max(l)
print (counter)
