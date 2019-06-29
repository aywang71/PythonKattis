#https://open.kattis.com/problems/licensetolaunch
#input format
n = int(input())
items = input().split(' ')
#variable to store lowest thing
lowest = 0
#debugging
print(items)
#for loop for each item in the list
for i in range (0,len(items)):
  items[i] = int(items[i])
  #updates the lowest variable
  if items[i]<items[lowest]:
    lowest = i
#output format
print(lowest)
