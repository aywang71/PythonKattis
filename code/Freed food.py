#https://open.kattis.com/problems/freefood

#input for n times
n = int(input())
#makes an empty array
day_year = []
#filles array, array index is the day of year
for i in range (0,365):
  day_year.append(0)
#debugging
print(day_year)
#asks for n input
for i in range (0,n):
  #input and format of start and end
  start_day,end_day = input().split(' ')
  start_day = int(start_day)
  end_day = int(end_day)
  #adds the occurence counter to index value
  for i in range (start_day-1,end_day):
    day_year[i] += 1
#debugging
print(day_year)
#count made for final tally
count = 0
#output format
for i in range (0,len(day_year)):
  if day_year[i]>=1:
    count += 1
print(count)