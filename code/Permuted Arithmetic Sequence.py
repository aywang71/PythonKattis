#https://open.kattis.com/problems/permutedarithmeticsequence

#input iteration
n = int(input())

#checks if they are in order
def classify (sequence,order):
  rate = (order[-1]-order[0])/(sequence[0]-1)
  #debugging
  print('items:',order[-1],order[0],sequence[0]-1,rate)
  for i in range (0,len(order)-1):
    if (order[i]+rate) == (order[i+1]):
      continue
    return False
  return True
#goes through iteration
for i in range (0,n):
  #inputs a sequence
  sequence = input().split(' ')
  for i in range (0,len(sequence)):
    sequence[i] = int(sequence[i])
  #order is just sequence without the length in the beginning
  order = sequence[1:]
  #output
  if classify(sequence,order):
    print('arithmetic')
  #we can check if its permuted by sorting it
  elif classify(sequence,sorted(order)):
    print('permuted arithmetic')
  else:
    print('non-arithmetic')