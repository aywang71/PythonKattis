#https://open.kattis.com/problems/everywhere
# sets up variable n for inital input
n = int(input())
# sets up places list for storage of subsets
places = []
# sets up b list of the initla subset values
b =[]
# runs this n times 
for i in range (0,n):
  # asks for input 
  x = int(input())
  # resets list b every time upper loop is run
  b = []
  # nested for loop to get from 0 to integer x
  for a in range (0,x):
    # prompts again for x input, as string
    x = input()
    # appends this to list b
    # this means x (integer) values of x (string) are on b
    b.append(x)
  # appends a list to a list, a nested list
  places.append(b)
# a nested list is important since we don't want to crete new lists, and we can cite these nested lists from inside the list

# a for loop for w in n
for w in range (0,n):
  # a new set for converting each sublist in places to a set
  # a set is a list but only unique values
  set_places = set(places[w])
  # finds length, therefore the unique values in places, which are now a set
  print(len(set_places))


