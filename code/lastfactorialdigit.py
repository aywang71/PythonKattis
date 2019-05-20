#https://open.kattis.com/problems/lastfactorialdigit
#input for number of times to run loop
n = int(input())
#sets list for storage of last digit values
l=[]
# for loop of n
for i in range(0,n):
  #variable x to ask input
  x = int(input())
  #resets factorial every iteration of the loop
  factorial = 1
  # a nested for loop to calculate factorial for x
  for i in range (1,x+1):
    factorial = factorial * i
    #DEBUGGING; it prints out each update of the factorial
    print(factorial)
  #converts the factorial to string so that the string can be sliced
  factorial = str(factorial)
  #appends the slice to the list
  l.append(factorial[-1])
#DEBUGGING; prints list 
print(l)
#for loop to print list values 
for x in range (0,n):
  print(l[x])

