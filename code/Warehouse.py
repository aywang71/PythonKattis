#https://open.kattis.com/problems/warehouse

#iteration input
n = int(input())
for i in range (0,n):
  #further iteration input
  x = int(input())
  #resets base lists
  numbers = []
  items = []
  #more input
  for x in range (0,x):
    inputs = input().split(' ')
    #adds existing product to older list
    if inputs[0] in items:
      numbers[items.index(inputs[0])] += int(inputs[1])
    #otherwise appends to new list
    else:
      items.append(inputs[0])
      numbers.append(int(inputs[1]))
  #to sort numbers and items into pairs
  pairs = []
  #puts them into the pair list
  for i in range (0,len(numbers)):
    x = [items[i],numbers[i]]
    pairs.append(x)
  #sorts pairs
  # sorts by key of x[0]
  pairs.sort(key = lambda x: x[0])
  # sorts in descending order by x[1]
  pairs.sort(key = lambda x: x[1], reverse = True)
  

  #output
  print(len(items))
  for i in pairs:
    i[1] = str(i[1])
    print(' '.join(i))

