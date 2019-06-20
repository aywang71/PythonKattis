#https://open.kattis.com/problems/datum
#input format
day, month = input().split(' ')
#converts to integer
day = int(day)
month = int(month)
#array for days in months
month_days = [0,31,28,31,30,31,30,31,31,30,31,30]
#counts days passed
days_elapsed = sum(month_days[0:month]) + day
#debugged
print(days_elapsed)
#finds remainder
weekday = days_elapsed%7
#output format if statement
if weekday == 1:
  print("Thursday")
elif weekday == 2:
  print("Friday")
elif weekday == 3:
  print("Saturday")
elif weekday == 4:
  print("Sunday")
elif weekday == 5:
  print("Monday")
elif weekday == 6:
  print("Tuesday")
elif weekday == 0:
  print("Wednesday")
