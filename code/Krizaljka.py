#https://open.kattis.com/problems/krizaljka

#needed as a deepcopy
import copy
#inputs
horizontal, vertical = input().split(' ')
crossword = []
temp = []
#creates crossword
for x in range (0,len(horizontal)):
  temp.append('.')
for i in range (0,len(vertical)):
  #makes each row a deepcopy and unique
  crossword.append(copy.deepcopy(temp))
#debugging
print(crossword)
#finds first occurance of similar
for i in horizontal:
  if i in vertical:
    similar = i
    horiz_sim = horizontal.index(i)
    vert_sim = vertical.index(i)
    break
#debugging
print(horiz_sim)
print(vert_sim)
#pops and inserts row
crossword.pop(vert_sim)
crossword.insert(vert_sim,list(horizontal))
#debugging
print(crossword)
#replaces along column
for i in range (0,len(vertical)):
  crossword[i][horiz_sim] = vertical[i]
#outputs
for i in range (0,len(crossword)):
  print(''.join(crossword[i]))