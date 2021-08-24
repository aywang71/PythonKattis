#https://open.kattis.com/problems/commercials

#input
breaks, price = input().split(' ')
breaks = int(breaks)
price = int(price)
listeners = input().split(' ')
#init max list
maxs = [int(listeners[0])-price]
#sets into max
for i in range (1,breaks):
  listeners[i] = int(listeners[i]) -price
  tot = max([maxs[i-1] + listeners[i],listeners[i]])
  maxs.append(tot)
#debugging
print(maxs)
#output
print(max(maxs))


