#https://open.kattis.com/problems/parking2

#input for iterations of loop
n = int(input())
#list for storage
distances = []
#n iterations begin
for i in range (0,n):
  #number of stores (doesn't matter)
  stores = int(input())
  #store_number is the indexes of the stores
  store_number = input().split(' ')
  #converts store_number items to integer
  for i in range (0,len(store_number)):
    store_number[i] = int(store_number[i])
  #finds min and max
  minimum = min(store_number)
  #print(minimum)
  maximum = max(store_number)
  #print(maximum)
  #distance is 2 times max-min
  distance = 2* (maximum-minimum)
  #puts distance into distances array
  distances.append(distance)
#output formatting
for i in range (0,len(distances)):
  print(distances[i])