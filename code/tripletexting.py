#https://open.kattis.com/problems/tripletexting

n = input()

i = int(len(n)/3)

for x in range(0,len(n), i):
  #print(n[x:(x+i)])
  if n.count(n[x:(x+i)]) >= 2:
    print(n[x:(x+i)])
    break
