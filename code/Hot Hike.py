#https://open.kattis.com/problems/hothike

#days
n = int(input())
#list for days
days = [int(i) for i in input().split(' ')]

#output
mini = [0,100]

#iteration
for i in range(0,len(days)-2):
  #finds the days
  temp_max = max([days[i],days[i+2]])
  #debugging
  print('temp_max:',temp_max)
  #replacement
  if temp_max < mini[1]:
    mini = [i+1,temp_max]
    #debugging
    print('out updated:',mini)
#data formatting
mini = [str(mini[0]),str(mini[1])]
#output
print(' '.join(mini))