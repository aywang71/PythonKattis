#https://open.kattis.com/problems/oddgnome

#input
n = int(input())
for i in range (0,n):
  #more input
  indexes = input().split(' ')
  #removes number and last
  del indexes[0]
  del indexes[-1]
  #sets x to first value
  x= int(indexes[0])
  for i in range(1,len(indexes)):
    #checks for order
    if x == int(indexes[i]) -1:
      #if ordered set x to current index
      x = int(indexes[i])
      continue
    else:
      #since lists start at 0
      print(i+1)
      break
  #debugging
  print(indexes)