#https://open.kattis.com/problems/babybites

#input formats
n = int(input())
bites = input().split(' ')
#list for n 
numbers = []
#appends n to numbers list
for i in range (1,n+1):
  numbers.append(i)
#debugging
print(numbers)
#length not equal is our first tip-off
if len(bites) != len(numbers):
  print('something is fishy')
else:
  #main code body
  i = 0
  #sets mumbles away
  for i in range (0,len(bites)):
    if bites[i] == 'mumble':
      bites[i] = numbers[i]
      #debugging
      print(bites)
#boolean to test print
correct = True
#data conversion
for i in range (0,len(bites)):
  bites[i] = int(bites[i])
#debugging
print(bites)
print(numbers)
#output format
for i in range (0,len(numbers)):
  if bites[i] == numbers[i]:
    continue
  else:
    #makes boolean false so last if doesn't run
    print('something is fishy')
    correct = False
    break

if correct == True:
  print('makes sense')    