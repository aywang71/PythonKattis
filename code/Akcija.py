#https://open.kattis.com/problems/akcija

#iteration input
n = int(input())
prices = []
#runs iterations
for i in range (0,n):
  #prices inputs
  price = int(input())
  prices.append(price)
#reverses prices
prices.sort(reverse=True)
#debugging
print(prices)
minimum = 0
#sets 0 to every third number
for i in range (2,n,3):
  prices[i] = 0
#debugging
print(prices)
#output
print(sum(prices))