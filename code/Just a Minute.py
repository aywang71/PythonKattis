#https://open.kattis.com/problems/justaminute

#iteration input
n = int(input())
#lists for averages, minutes recorded, and seconds recorded (future input)
actual_conversion = []
minutes = []
seconds = []

for i in range (0,n):
  #further input and data formatting
  minutes_shown, seconds_waited = input().split(' ')
  minutes_shown = int(minutes_shown)
  #adds minutes to minites list
  minutes.append(minutes_shown)
  seconds_waited = int(seconds_waited)
  seconds.append(seconds_waited)
  #conversion
  actual_conversion.append(seconds_waited/(minutes_shown*60))

#finds average
average = sum(seconds)/sum(minutes)/60
#output format
if average <= 1:
  print('measurement error')
else:
  print(average)

