#https://open.kattis.com/problems/boatparts

#inputs for parts and days
number, days = input().split(' ')
number = int(number)
days = int(days)
parts = []
boolean = True
#gets one part per day
for i in range (1,days+1):
  string = input()
  if string in parts:
    #debugging
    print('already replaced')
    continue
  else:
    #debugging
    print('not replaced')
    #adds this new part to the parts list
    parts.append(string)
  #if the amount of parts is done, get i and print
  if len(parts) == number:
    print(i)
    boolean = False
    break
#if the parts aren't enough, paradox avoided
if boolean == True:
  print('paradox avoided')

  
