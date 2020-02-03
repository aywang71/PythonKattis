#https://open.kattis.com/problems/hothike

n = int(input())
days = [int(i) for i in input().split(' ')]

mini = [0,100]

for i in range(0,len(days)-1]:
  temp_min = min([days[i],days[i+2]])
  print('temp_min:',temp_min)
  if temp_min < mini[1]:
    mini = [i,temp_min])
    print('out updated:',mini)
print(' '.join(mini))

