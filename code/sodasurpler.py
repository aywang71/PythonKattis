#https://open.kattis.com/problems/sodasurpler

#inputs
sodas, found, recycle = input().split(' ')
#sodas are equal to found as we only want to find recycleable items
sodas = int(sodas)
sodas += int(found)
recycle = int(recycle)
count = 0
static_count = 0
#loops until no more can be recycled
while True:
  if sodas//recycle  < 1:
    break
  static_count = sodas//recycle
  count += static_count
  sodas = sodas%recycle
  sodas += static_count
  #print(sodas)
  #print(count)
print(count)
