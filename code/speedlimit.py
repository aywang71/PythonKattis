#https://open.kattis.com/problems/speedlimit
#this is the array for the final output
distance_array = []
# you can have a total of 10 data sets
for i in range (0,10):
  #asks for input
  n = int(input())
  #simulates a posttest loop, if the n== -1 (FLAG) it stops program
  if n ==  -1:
    break 
  #clears speed and time lists
  speed = []
  time = []
  #resets distance to 0
  distance = 0
  # in the rane to n, prompt for speed, time
  for i in range (0,n):
   x,y = input().split(' ')
   # integer and files into lists
   x = int(x)
   y = int(y)
   speed.append(x)
   time.append(y)
  #debugging
  print(speed)
  print(time)
  #after this we take the lenght of either list, and file it into the distance array
  for i in range (0,len(speed)):
    if i == 0:
     distance = speed[i]*time[i]
    else:
     distance += speed[i] * (time[i]-time[i-1])
  distance_array.append(distance)
#this is the output format
for i in range (0,len(distance_array)):
  print(distance_array[i], " miles")
