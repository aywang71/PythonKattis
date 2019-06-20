#https://open.kattis.com/problems/batterup
#input format
n= int(input())]
#splits another input by spaces
x = input().split(' ')
#sum for average calculation
sum = 0

#removes all the -1 in the list
for i in range (0,x.count('-1')):
  x.remove('-1')
#converts each value to integer
for i in range (0,len(x)):
  x[i] = int(x[i])
# adds each value of the integer list to the sum
for i in range (0,len(x)):
  sum += x[i]
# calcualte average
print(sum/len(x))
