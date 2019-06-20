#https://open.kattis.com/problems/symmetricorder
#storage values
epic_list_left = []
epic_list_right =[]
set_count = 0
#python's posttest loop
while True:
  #input n
  n = int(input())
  #checks n value
  if n == 0:
    break
  #actual code here
  else:
    #count +1 for the set display
    set_count += 1
    #resets name list, left, and right
    name_list = []
    name_left = []
    name_right = []
    # gets n name inputs
    for i in range(0,n):
      name = input()
      #appends list name
      name_list.append(name)
    #to respective left right values
    for i in range (0,n):
      if i%2 == 0:
        name_left.append(name_list[i])
      else:
        name_right.append(name_list[i])
    #nest list to epic left and epic right
    epic_list_left.append(name_left)
    epic_list_right.append(name_right)
#debugging
print(epic_list_left)
#debugging
print(epic_list_right)
#output format
for i in range (1,set_count+1):
  #prints for sets
  print('SET',i)
  #prints for left list; from 0 to i-1 (as i starts at 1)
  for x in range (0,len(epic_list_left[i-1])):
    #prints nested list left
    print(epic_list_left[i-1][x])
  #prints for right list; from 0 to i-1(as i starts at 1)
  for y in range (0,len(epic_list_right[i-1])):
    #prints the list right backwards
    print(epic_list_right[i-1][-(y+1)])
  


