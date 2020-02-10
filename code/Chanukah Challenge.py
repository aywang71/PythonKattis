#https://open.kattis.com/problems/chanukah

#gets iteration number
iteration = int(input())
#runs loop
for i in range (0,iteration):
  #inputs on data number and days
  iteration_number,days = input().split(' ')
  days = int(days)
  #formula for sequcence sum
  candles = (1+days)/2*days
  #adds days
  candles += days
  #formats and outputs
  print('%s %i'%(iteration_number,candles))