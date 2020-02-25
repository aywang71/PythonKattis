#https://open.kattis.com/problems/bus

#iteration input
n = int(input())
for i in range (0,n):
  #more input
  turns = int(input()) -1
  #at least one person on bus
  people = 1
  #work backward until reached first stop
  while turns != 0:
    #makes turns one less
    turns -= 1
    #first adds half
    people += 0.5
    #doubles
    people = people *2
  #output
  print(int(people))
