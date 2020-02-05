#https://open.kattis.com/problems/volim

#starting position
start = int(input())
#array of positions
positions = [1,2,3,4,5,6,7,8]
#from array, which starts at index 0
current_position = positions[start-1]
#number of questions
questions = int(input())
#total time
time_total = 210
#passed time
time_elapsed = 0
#asks n questions
for i in range(0,questions):
  #further input 
  time, response = input().split(' ')
  #resets correct boolean
  correct = False
  time = int(time)
  #if its correct, correct = True
  if response == "T":
    time_elapsed += time
    correct = True
    #debugging
    print("Good:",time_elapsed)
  else:
    time_elapsed += time
    #debugging
    print("Bad:",time_elapsed)
  #if time is up
  if time_elapsed >=time_total:
    print(current_position)
    #debugging
    print('broke:', time_elapsed)
    break
  #if its correct, change places
  if correct == True:
    if current_position == 8:
      current_position = 1
    else:
      current_position += 1
  
