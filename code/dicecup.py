#https://open.kattis.com/problems/dicecup
#input format 
die1, die2 = input().split(' ')
#converts to integer
die1 = int(die1)
die2 = int(die2)
#makes the number of 0s in sum list equa to the 2 die +2 for 0 
sum = [0] * (die1 + die2 + 1)
#maximum storage value
max_DRN = 0
#nested for loop to control the list index, which is the sums; every time sum[k] is called you +1 to it
for i in range (1, die1 +1):
  for j in range (1, die2 + 1): 
    k = i + j
    sum[k] = sum[k] + 1
    #if your sum[k] is larger than the currently set max_DRN, replace it
    if (sum[k] > max_DRN):
      max_DRN = sum[k]
#if any number is equal to the max_DRN in the list, print its index value
for i in range (0, len(sum)) :
  if (sum[i] == max_DRN ) :
    print(i)
