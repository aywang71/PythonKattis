#https://open.kattis.com/problems/zanzibar
n= int(input())
sequence_list = []
extras_list = []
for i in range (0,n):
  sequence = input().split(' ')
  sequence.remove('0')
  sequence_list.append(sequence)
print(sequence_list)
for i in range (0,n):
  for x in range (0,len(sequence_list[i])):
    sequence_list[i][x]= int(sequence_list[i][x])
print(sequence_list)

for i in range (0,n):
  count = 0
  for x in range (0,len(sequence_list[i])-1):
    if sequence_list[i][x+1] > 2*sequence_list[i][x]:
      count += sequence_list[i][x+1]-(2*sequence_list[i][x])
      print(count)
  extras_list.append(count)

for i in range (0,len(extras_list)):
  print(extras_list[i])
