#https://open.kattis.com/problems/2naire
import math
while True:
  n, p = input().split(' ')
  n = int(n)
  p = float(p)
  if n == 0 and p == 0: break
  win = 2 ** n #total amount you could win
  for k in range(n-1,-1,-1): # go from last question to 0 
    thresh  = (2 ** k)/win #you basically get 2 ** (k-n) - this is showing the fraction of total money you'll miss out on if you end at question k 
    if p >= thresh : #if the probability that you get the question right is greater than or equal to the amount of money you'll miss out on - basically says its advantageous to answer the early questions 
      win  = (p+1)/2 * win  #the amount you win ON AVERAGE(because in all possible outcomes you fail a portion of them (1-p of them to be exact)) as a portion of the total you could win
    else: #this case will trigger on the later questions - when it gets to 1/2, or 1/4, etc. 
      win  = (2 ** k) * (thresh -p)/(1-p) + win  * (thresh +1)/2 * (1-thresh )/(1-p)
      #first: the amount you could win at k questions, multiplied by the difference between probability and winning threshold, and then divided by the probability you get the question wrong 
      #second: some kind of formula I assume - which then ratios down win
  print("{:.3f}".format(win))