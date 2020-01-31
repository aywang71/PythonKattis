number,points,row = input().split(' ')
number = int(number)
points = int(points)
row = int(row)
name_score = {}
winners = []
for i in range (0,number):
  name = input()
  name_score[name] = 0
#print(name_score)
for i in range (0,row):
  data = input().split(" ")
  data[1] = int(data[1])
  name_score[data[0]] += data[1]
  if name_score[data[0]]>=points:
    if data[0] in winners:
      continue
    else:
      winners.append(data[0])
#print(name_score)
#print(winners)
if len(winners) == 0:
  print('No winner!')
else:
  for i in range (0,len(winners)):
    print('%s wins!'%(winners[i]))