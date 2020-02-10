#https://open.kattis.com/problems/soylent

#need math.ceil
import math
#iteration count
n = int(input())
for i in range (0,n):
  #calories
  calories = int(input())
  #integer output
  print(math.ceil(calories/400))