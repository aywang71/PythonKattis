#https://open.kattis.com/problems/redrover

#input
message = input()
# best length
best = len(message)
#nested for loop to find all possible combinations
for i in range (len(message)):
  for x in range (i+2,len(message)):
    #counts instances of that piece of string occuring
    count = message.count(message[i:x])
    #if its a lower length replace it
    if (len(message)-(count*(x-i))+count+x-i) < best:
      best = (len(message)-(count*(x-i))+count+x-i)
#output
print(best)