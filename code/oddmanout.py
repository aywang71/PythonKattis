#https://open.kattis.com/problems/oddmanout
#input format
test_cases = int(input())
#storage values
extra_list = []
#asks for a number from test_cases
for i in range (0,test_cases):
  #format of input
  guest_number = int(input())
  guest_id = input().split(' ')
  #nested for loop to append IDs without another same ID to extra_list
  for i in range (0,len(guest_id)):
    if guest_id.count(guest_id[i]) >1:
      continue
    else:
      extra_list.append(guest_id[i])
#debugging
print(extra_list)
#output format to print extra_list and index of extra_list
for i in range (0,len(extra_list)):
  number = i+1
  listID = extra_list[i]
  print('Case #%s: %s'%(number,listID))
