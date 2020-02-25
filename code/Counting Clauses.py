#https://open.kattis.com/problems/countingclauses

#inputs
x,y = input().split(' ')
inputs = []
for i in range (0,int(x)):
  row = input()
  inputs.append(row)
#output
if int(x) >=8:
  print('satisfactory')
else:
  print('unsatisfactory')