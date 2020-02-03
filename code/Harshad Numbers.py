#https://open.kattis.com/problems/harshadnumbers

#input prompt
n= int(input())
#for loop from n to max numbers
for i in range (n,1000000001):
  #number = i; placeholder
  number = i
  # i to string of i
  i = str(i)
  #convert to list
  i = list(i)
  #reset digit_sum to 0
  digit_sum = 0
  #adds each value of i to digit_sum
  for x in range(0,len(i)):
    i[x] = int(i[x])
    digit_sum += i[x]
  # if it %'s == 0, print number and break; else keep going
  if number%digit_sum ==0:
    print(number)
    break
  else:
    continue