#https://open.kattis.com/problems/friday

#runs to check for 13th and update starting date
def run(day_left,start,week):
  #boolean system for 13th checking
  boolean = False
  #no point to check if less than 13 days
  if day_left <13:
    pass
  else:
    #calculates the day of week on 13th
    thrt = week[(week.index(start)+5)%7]
    #debugging
    print('13:',thrt)
    #only if friday the 13th
    if thrt == 'fri':
      boolean = True
  #debugging
  print('days left:', day_left)
  #minimum calculations
  day_left = (day_left)%7
  #debugging
  print('days left:',day_left)
  #resets start value
  start = week[(week.index(start) + day_left)%7]
  #return
  return boolean, start

#iteration input
n = int(input())
for i in range (0,n):
  #resets 13th count
  count = 0
  #week for inputs later
  week = ['sun','mon','tue','wed','thu','fri','sat']
  #year always starts at sunday
  start = 'sun'
  #input
  days, months = input().split(' ')
  days = int(days)
  months = int(months)
  #days per month
  day_month = input().split(' ')
  # runs through each month
  for i in range (0,len(day_month)):
    day_left = int(day_month[i])
    #debugging
    print('start:',start)
    #runs 'run' function
    boolean, start = run(day_left,start,week)
    if boolean:
      #debugging
      print('month:',i)
      count += 1
  #output
  print(count)
