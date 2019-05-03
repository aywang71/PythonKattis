#https://open.kattis.com/problems/sevenwonders
#input format
n = list(input())
#storage values
tablet = 0
compass = 0
gear = 0
a =[]
minimum = 0
# for all n, add respective values to storage values
for i in range (0,len(n)):
  if n[i] == 'T':
    tablet+=1
  elif n[i] == 'C':
    compass+=1
  elif n[i] == 'G':
    gear+=1
#adds each value to list a
a.append(tablet)
a.append(compass)
a.append(gear)
# makes the minimum value the smallest value in a
minimum = min(a)
#output format
print((minimum*7) + (tablet * tablet) + (compass * compass) + (gear * gear))
