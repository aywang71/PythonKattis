#https://open.kattis.com/problems/transitwoes

#variable init stuff
start,total,stops = [int(i) for i in input().split(' ')]
travel = [int(i) for i in input().split(' ')]
t = 0
bus_time = [int(i) for i in input().split(' ')]
#instead of calculating seperatly we sum them because its still the same transit time from point to point
for i in range (len(bus_time)):
  travel[i+1] += bus_time[i]
interval = [int(i) for i in input().split(' ')]

#algorithm to calculate total time
for i in range (len(travel)):
  t += travel[i]
  #debug
  print("init time",t)
  if i == (len(travel) -1):
    break
  t += (interval[i] - t)%interval[i]
  #debug 
  print("time:", t)

if (t>total):
  print('no')
else:
  print('yes')