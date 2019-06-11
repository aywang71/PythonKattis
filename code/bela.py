#https://open.kattis.com/problems/bela
#Input syntax for number of hands and suite
n, dominant_suite = input().split()
# converts hands to integer
n = int(n)
# converts dominant suite to string
dominant_suite = str(dominant_suite)
# creates lists for fileing away point value and suite
point_value =[]
suite = []
#sum; output number
sum = 0
# for this range we prompt input X and split into respective lists
for i in range (0, n*4):
  x = input()
  suite.append(x[1])
  point_value.append(x[0])
#DEBUGGING
print(point_value)
print(suite)
# A for loop to run through everything in the list
for i in range (0,len(point_value)):
  #inital check for suite, as the lists are aligned
  if suite[i] == dominant_suite:
    # follows a set of points if the suite is the dominant suite
    if point_value[i] == "A":
      sum += 11
    elif point_value[i] == "K":
      sum += 4
    elif point_value[i] == "Q":
      sum += 3
    elif point_value[i] == "J":
      sum += 20
    elif point_value[i] == "T":
      sum += 10
    elif point_value[i] == "9":
      sum += 14
    else:
      continue
  #if the suite is not the dominant suite
  else:
    # a different set of points
    if point_value[i] == "A":
      sum += 11
    elif point_value[i] == "K":
      sum += 4
    elif point_value[i] == "Q":
      sum += 3
    elif point_value[i] == "J":
      sum += 2
    elif point_value[i] == "T":
      sum += 10
    else:
      continue

print(sum )

