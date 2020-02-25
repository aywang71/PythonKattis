#https://open.kattis.com/problems/earlywinter

#input format
years, time = input().split(' ')
years = int(years)
time = int(time)
#count for output
count = 0
#more input
times = input().split(' ')
#runs through times list backwards
for i in range (len(times)-1,-1,-1):
  #integer
  times[i] = int(times[i])
  #alters count variable
  if times[i] > time:
    count += 1
  elif times[i]<=time:
    count = 0
#output format
if count == len(times):
  print('It had never snowed this early!')
else:
  print("It hadn't snowed this early in %i years!"%(count))
