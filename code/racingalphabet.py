#https://open.kattis.com/problems/racingalphabet

#makes the circle
circle = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ '")
#iteration input
n = int(input())
for i in range (0,n):
  #string input 
  string = list(input())
  #sets up first base
  previous = circle.index(string[0])
  #total sum storage
  total = 0
  #for second character until last
  for i in range (1,len(string)):
    #current
    current = circle.index(string[i])
    #the two methods of distance finding
    distance1 = abs(previous-current)
    distance2 = len(circle)-distance1
    #finds lower distance
    distance = min([distance1,distance2])
    #debugging
    print(distance1,distance2,distance)
    # adds to total
    total += distance
    #sets up next block
    previous = current
  #after loop runs, runs total through conversion
  total = total * 6.73198425769 / 15
  #adds 1 second per character
  total += len(string)
  #output
  print(total)
