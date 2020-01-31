#http://open.kattis.com/problems/avion

#list input form
codes = []
out = []
for i in range (5):
  codes.append(input())
#find occurences of 'FBI' and append those list indexes + 1 to another list
for i in codes:
  if i.find('FBI') == -1:
    continue
  else:
    out.append(codes.index(i) +1)
#join' ' that list together
print(out.join(' '))