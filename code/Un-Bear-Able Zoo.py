#https://open.kattis.com/problems/zoo

#for sending list data
count = 0
#until 0 entered
while True:
  iteration = int(input())
  count += 1
  if iteration == 0:
    break
  #resets list
  animals = []
  #iteration amount of animals
  for i in range (0,iteration):
    #further input
    animal_name = input().split(' ')
    #formatting to get last species type
    animal = animal_name[-1]
    animal = animal.lower()
    animals.append(animal)
  #debugging
  print(animals)
  unique = sorted(list(set(animals)))
  #debugging
  print(unique)
  #output
  print('List %i:'%(count))
  for i in range (0,len(unique)):
    #more output
    print("%s | %i"%(unique[i],animals.count(unique[i])))

