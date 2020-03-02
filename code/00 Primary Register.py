def check(values,tubes):
  for i in range (len(values)):
    if values[i] == (tubes[i]-1):
      continue
    else:
      return False
    return True

def increment(values,tubes):
  value = 0
  #print(values[value],value)
  while ((values[value]+1) >= tubes[value]):
    #print('passed index:',value,values[value])
    value += 1
  values[value] = values[value] +1
  values = reset(values,value)
  #print(values)
  return values

def reset(values,value):
  for i in range(value):
    values[i] = 0
  return values

#https://open.kattis.com/contests/dkft54/problems/register
tubes = [int(i) for i in "2, 3, 5, 7, 11, 13, 17,  19".split(", ")]
top = 2 * 3 * 5 * 7 * 11 * 13 * 17 *19
#print('top value:',top)

values = [int(i) for i in input().split(' ')]

#print('inputs:',values)
#print('123456:',tubes)

out = 1

for i in range (len(tubes)):
  out = out * (tubes[i]-values[i])
print(out-1)