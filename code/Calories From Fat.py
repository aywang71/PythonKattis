#https://open.kattis.com/problems/calories

def percenter (calories, stat, fat, percent):
  #finds the total number of calories
  calories = 100/(100-percent) * calories
  #if the fat calories is a percent, multiply through the total
  if stat[0][-1] == '%':
    fat = calories * int(stat[0][:-1])/100
  #return
  return calories, fat

#EOF reading
import sys
#long term storage, resets every output
calorie = 0
fats = 0
percent = 0
for line in sys.stdin:
  #short term storage, for calculating with percents, resets every input
  percent = 0
  calories = 0
  fat = 0
  #strips '\n' from input line
  stat = line.rstrip().split(' ')
  #output happens when reset with '-'
  if stat[0] == '-':
    #try catch will tell when the input case is over, as two '-' shows the input case is over
    try:
      #rounds and strings for output
      output = str(round(fats/calorie*100))
      #output
      print(''.join([output,'%']))
      #resets long term counters
      calorie = 0
      fats = 0
      continue
    except:
      break
  #debugging
  #print('stat:',stat)
  for i in range(5):
    if stat[i][-1] == 'g':
      #debugging: checks if the program reaches here
      #print('gram activate')
      if i == 0:
        fat += 9 * int(stat[i][:-1])
        calories += 9 * int(stat[i][:-1])
      elif i == 1:
        calories += 4 * int(stat[i][:-1])
      elif i == 2:
        calories += 4 * int(stat[i][:-1])
      elif i == 3:
        calories += 4 * int(stat[i][:-1])
      elif i == 4: 
        calories += 7 * int(stat[i][:-1])
    elif stat[i][-1] == 'C':
      #debugging: checks if the program reaches here
      #print('calorie activate')
      if i == 0:
        fat += int(stat[i][:-1])
        calories += int(stat[i][:-1])
      elif i == 1:
        calories += int(stat[i][:-1])
      elif i == 2:
        calories += int(stat[i][:-1])
      elif i == 3:
        calories += int(stat[i][:-1])
      elif i == 4: 
        calories += int(stat[i][:-1])
    else:
      percent += int(stat[i][:-1])
    #debugging
    #print('part:',int(stat[i][:-1]))
    #print('change:',calories,fat)
  #runs the percents through the 'percenter' function to find values
  if percent != 0:
    calories, fat = percenter(calories, stat, fat, percent)
#adds short term to long term
  #debugging
  #print('calories',calories)
  calorie += calories
  #debugging
  #print('fat',fat)
  fats += fat
  

    