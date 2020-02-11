#https://open.kattis.com/problems/securedoors

#iteration input
n= int(input())
entered = []
#runs loops
for i in range (0,n):
  #status input
  state, name = input().split(' ')
  #multi stage if statement to filter through name
  if (state == 'entry') and (name not in entered):
    entered.append(name)
    print(name,'entered')
  elif (state == 'entry') and (name in entered):
    print(name, 'entered (ANOMALY)')
  elif (state == 'exit') and (name in entered):
    entered.remove(name)
    print(name,'exited')
  elif (state == 'exit') and (name not in entered):
    print(name, 'exited (ANOMALY)')
  #debugging
  print(entered)

  