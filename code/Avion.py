#http://open.kattis.com/problems/avion

#list input form
codes = []
out = []
for i in range (5):
  if input().find('FBI') == -1:
    continue
  else:
    out.append(str(i+1))
#join' ' that list together
if len(out) == 0:
  print('HE GOT AWAY!')
else:
  print(' '.join(out))