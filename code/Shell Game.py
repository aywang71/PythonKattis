#http://usaco.org/index.php?page=viewproblem&cpid=867

#input format
n = int(input())
#three test cases for possible ball start locations
test1_cups = [1,0,0]
test2_cups = [0,1,0]
test3_cups = [0,0,1]
#score counter
scores = [0,0,0]
#iteration count
for i in range (0,n):
  #more input for switches and formatting
  switch1, switch2, guess = input().split(' ')
  switch1 = int(switch1)
  switch2 = int(switch2)
  guess = int(guess)
  #switches locations of all elements switched
  test1_cups[switch1-1], test1_cups[switch2-1] = test1_cups[switch2-1],test1_cups[switch1-1]
  #debugging
  #print('case 1:',test1_cups)
  test2_cups[switch1-1], test2_cups[switch2-1] = test2_cups[switch2-1],test2_cups[switch1-1]
  #debugging
  #print('case 2:',test2_cups)
  test3_cups[switch1-1], test3_cups[switch2-1] = test3_cups[switch2-1],test3_cups[switch1-1]
  #debugging
  #print('case 3:',test3_cups)
  #counts guess score
  if test1_cups[guess-1] == 1:
    scores[0] += 1
  if test2_cups[guess-1] == 1:
    scores[1] += 1
  if test3_cups[guess-1] == 1:
    scores[2] += 1
#output format
print(max(scores))

