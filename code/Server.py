#https://open.kattis.com/problems/server

#input and formatting
cases, minutes = input().split(' ')
minutes = int(minutes)
times = input().split(' ')
#test data
print(times)
for i in range (0,len(times)):
  times[i] = int(times[i])
#test data
print(times)
time_elapsed = 0
count = 0
for i in range (0,len(times)):
  time_elapsed += times[i]
  if time_elapsed > minutes:
    break
  count +=1
#output format
print(count)