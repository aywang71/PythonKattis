#https://open.kattis.com/problems/cups

#input format
n = int(input())
#pair list
pair_list = []
#gets n pairs
for i in range (0,n):
  #input 
  x, y = input().split(' ')
  #resets pair list
  abridged_list= []
  #try statement for validation
  try:
    x = int(x)
    abridged_list.append(x/2)
    abridged_list.append(y)
  except ValueError:
    y = int(y)
    abridged_list.append(y)
    abridged_list.append(x)
  pair_list.append(abridged_list)
#debugging
print(pair_list)
#sorts list with first value
pair_list.sort()
#debugging
print(pair_list)
#output format
for i in range (0,n):
  print(pair_list[i][1])