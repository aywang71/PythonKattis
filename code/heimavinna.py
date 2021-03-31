#https://open.kattis.com/problems/heimavinna

n = input().split(';')

#print(n)

start = 0
end = 0 
tot = 0

for i in n:
  i = i.split('-')
  #print(i)
  if len(i) > 1: tot += int(i[1]) - int(i[0]) + 1
  else: tot += 1

print(tot)