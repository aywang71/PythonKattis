#https://open.kattis.com/problems/baconeggsandspam

while True:
  #iteration input 
  n = int(input())
  #breakage point
  if n == 0:
    break
  #resets lists
  items = []
  people = []
  for i in range (0,n):
    #more input
    string = input().split(' ')
    for x in range (1,len(string)):
      #nested lists and append
      if string[x] not in items:  
        items.append(string[x])
        iterative = [string[0]]
        people.append(iterative)
      else:
        people[items.index(string[x])].append(string[0])
  #debugging
  print(items)
  print(people)
  pairs = []
  #pairs up people and items 
  for i in range (0,len(items)):
    x = [items[i],sorted(people[i])]
    pairs.append(x)
  pairs.sort(key = lambda x: x[0])
  #debugging
  print(pairs)
  #output
  for i in pairs:
    print(i[0],' '.join(i[1]))
  print('\n')

