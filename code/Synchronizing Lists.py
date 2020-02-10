#https://open.kattis.com/problems/synchronizinglists

#repeat
while True:
  #input iteration
  n = int(input())
  #break point
  if n == 0:
    break
  #lists for ordering and sorting
  list1_order = []
  list1_sorted = []
  list2_sorted = []
  #gets most list values
  for i in range (0,2*n):
    #more inputs
    number = int(input())
    #either appends to first or second list
    if i <n:
      list1_order.append(number)
    else:
      list2_sorted.append(number)
  #sorts lists to later compare index values
  list1_sorted = sorted(list1_order)
  list2_sorted = sorted(list2_sorted)
  #debugging
  print(list2_sorted) 
  #prints by index of reference in first sorted list to second
  for i in range(0,len(list1_order)):
    print(list2_sorted[list1_sorted.index(list1_order[i])])
  #debugging
  print(list1_order)
