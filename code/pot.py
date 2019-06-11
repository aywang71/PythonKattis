#https://open.kattis.com/problems/pot
#input 
n = int(input())
#storage values for number, power, and total
numbers_list = []
powers_list = []
sum = 0
# asks for n inputs, adds the last x to powers, removes last item, and appends rest of list to numbers list
for i in range (0,n):
  x = list(input())
  #debugging
  print(x)
  powers_list.append(x[-1])
  #debugging
  del x[-1]
  print(x)
  numbers_list.append(''.join(x))
#converts everything to integer
for i in range (0,len(numbers_list)):
  numbers_list[i] = int(numbers_list[i])
  powers_list[i] = int(powers_list[i])
#debugging
print(numbers_list)
print(powers_list)
#sums the powers in each list
for i in range(0,len(numbers_list)):
  sum += numbers_list[i]**powers_list[i]
print(sum)
