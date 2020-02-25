#https://open.kattis.com/problems/peragrams

#input
string = list(input())
v1 = []
v2 = []
#adds odd amounts of letters to version 1 (v1)
for i in range (0,len(string)):
  #debugging
  print(i)
  if string.count(string[i])%2 == 0:
    continue
  else:
    v1.append(string[i])
  #debugging
  print(string)
#adds one copy of each thing from version 1 (v1) to version 2 (v2)
for i in range (0,len(v1)):
  if v1[i] not in v2:
    v2.append(v1[i])
#output
if (len(v2)-1 == 0) or (len(v2)==0):
  print(0)
else:
  print(len(v2)-1)
