#https://open.kattis.com/problems/cardtrick2

#for deepcopy
import copy
#iteration input
n = int(input())
for i in range (n):
  #input number of cards
  cards = int(input())
  order = []
  #makes empty list with same number of items as cards variable
  for i in range (cards):
    #each index value represents the original index element
    order.append(i)
  #starts at list index 1
  pos = 1
  output = copy.deepcopy(order)
  #if its only 1 card, make the first '1', otherwise make the second '1'
  if len(output) == 1:
    output[0] = '1'
  else:
    output[1] = '1'
    order.pop(1)
  #for range of cards
  for i in range (2,cards+1):
    #finds the new card position
    pos = (pos +i)%len(order)
    #debugging
    print(pos)
    #sets that equal to what the element reads
    output[order[pos]] = str(i)
    order.pop(pos)
    #debugging
    print(order,output)
  #output
  print(' '.join(output))
