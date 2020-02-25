#https://open.kattis.com/problems/aboveaverage

#finds the amount of 0s missing from the output
def missing (output):
  #splits to find decimal portion
  counter = str(output).split('.')
  #debugging
  print(counter)
  valued = counter[1]
  #debugging
  print(valued)
  #return portion
  if len(valued) == 1:
    return 2
  elif len(valued) == 2:
    return 1
  else:
    return 0

#iteration input
n = int(input())
for i in range (0,n):
  #count for storing amount of people
  count = 0
  #input
  numbers = input().split(' ')
  #conversion to integer
  for i in range (0,len(numbers)):
    numbers[i] = int(numbers[i])
  #to store amount of people
  number = numbers[0]
  #debugging
  print('amount:', number)
  #takes out the first value, which is the amount of people
  numbers.pop(0)
  #debugging
  print('students:', numbers)
  #average
  average = sum(numbers)/number
  #debugging
  print('average:',average)
  #finds amount of people over average
  for i in numbers:
    if i > average:
      count += 1
  #debugging
  print('kids:', count)
  #finds percentage for kids over average
  percent = round((count/number*100),3)
  #debugging
  print(percent)
  #runs missing function
  inserted = missing(percent)
  #makes output formatting
  output = list(str(percent) + '%')
  #adds more 0s
  if inserted > 0:
    for i in range (0,inserted):
      output.insert(-1,'0')
  #outputs
  print(''.join(output))
