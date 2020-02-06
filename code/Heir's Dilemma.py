#https://open.kattis.com/problems/heirsdilemma

#input values
start, end = input().split(' ')
start = int(start)
end = int(end)
count = 0
#counts from start to end
for i in range (start,end+1):
  #resets booleans with every iteration
  double =  False
  mod = True
  i = str(i)
  number = int(i)
  no_zeroes = []
  #no 0s
  if '0' in i:
    continue
  # looks for doubles
  for x in range (0,len(i)):
    if i.count(i[x]) != 1:
      double = True
      break
  #executs for mods
  if double == False:
    for x in range (0,len(i)):
      num = int(i[x])
      if number%num != 0:
        mod = False
        break
    #counts
    if mod == True:
      count += 1
#output
print(count)
