#https://open.kattis.com/problems/missingnumbers

#starts storage lists
numbers = []
output = [] 

#gets a list of numbers
for i in range(int(input())):
  numbers.append(int(input()))
#debugging
print('numbers:',numbers)

#checks for range of numbers
for i in range(1,max(numbers)+1):
  if i in numbers:
    continue
  else:
    output.append(i)

#output 
if len(output) == 0:
  print('good job')
else:
  for i in output:
    print(i) 
