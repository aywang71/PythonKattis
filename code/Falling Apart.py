#https://open.kattis.com/problems/fallingapart

#number of pieces (not used)
pieces = int(input())
#values of pieces and formatting
values = input().split(' ')
for i in range (0,len(values)):
  values[i] = int(values[i])
#reverses in greatest to least
values.sort(reverse=True)
#debugging
print(values)
#values of a and b
a = 0
b = 0
#the value in the list
count = 0
#runs through and adds every other
while count != len(values):
  if count%2 == 0:
    a +=values[count]
  else:
    b += values[count]
  count += 1
#output
print(a)
print(b)
  