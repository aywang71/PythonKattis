#https://open.kattis.com/problems/kafkaesque

clerks = []

for i in range (int(input())):
  clerks.append(int(input()))

#debugging
print('list:',clerks)
count = 1

for i in range (0,len(clerks)-1):
  if clerks[i+1] > clerks[i]:
    continue
  else:
    count += 1
print(count)
