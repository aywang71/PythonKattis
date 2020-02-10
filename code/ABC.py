#https://open.kattis.com/problems/abc

# input of sequence
numbers = input().split(' ')
for i in range (0,3):
  numbers[i] = int(numbers[i])
numbers = sorted(numbers)
#debugging
print(numbers)
#order of items
order = list(input())
#debugging
print(order)
#list for output
number_list = [0,0,0]
for i in range (0,3):
  #replaces items into number_list
  if order[i] == "A":
    number_list[i] = str(numbers[0])
  if order[i] == "B":
    number_list[i] = str(numbers[1])
  if order[i] == "C":
    number_list[i] = str(numbers[2])
#debugging
print(number_list)
#output
print(' '.join(number_list))
