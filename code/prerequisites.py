#https://open.kattis.com/problems/prerequisites

#until input is 0
while True:
  n = input().split(' ')
  #debugging
  print(n)
  if n[0] == '0':
    break
  #this will restart the loop because when 'no' is printed, the loop restarts but there is still more course requirements
  if len(n) != 2:
    continue
  #the courses that he took
  courses = input().split(' ')
  #out is wether or not to print yes
  out = True
  #goes through iteration input
  for i in range (0,int(n[1])):
    #category of courses
    cat = input().split(' ')
    #records how many courses taken in that catagory
    count = 0
    #minimum number of courses needed per catagory
    mini = int(cat[1])
    #goes through to find which courses per catagory were taken
    for i in range (2,len(cat)):
      if cat[i] in courses:
        count += 1
        #if you've taken enough don't count any more
        if count == mini:
          break
    #after going through, 
    if count < mini:
      print('no')
      out = False
      break
  #final output
  if out == True:
    print('yes')
