#https://open.kattis.com/problems/kornislav

#input for 4 sides
numbers = input().split(' ')
#sorts inputs
numbers.sort()
#debugging
print(numbers)
#conversion to integer
for i in  range(0,len(numbers)):
  numbers[i] = int(numbers[i])
#output
print(numbers[0]*numbers[2])
