#https://open.kattis.com/problems/parking

#input format
price1, price2, price3 = input().split(' ')
price1 = int(price1)
price2 = int(price2)
price3 = int(price3)
start1, end1 = input().split(' ')
start1 = int(start1)
end1 = int(end1)
start2, end2 = input().split(' ')
start2 = int(start2)
end2 = int(end2)
start3, end3 = input().split(' ')
start3 = int(start3)
end3 = int(end3)
timeline =[]

#creates empty list with max values
temp = [end1,end2,end3]
iterate = max(temp)
for i in range (0,iterate):
  timeline.append(0)
#goes through to add trucks per minute
for i in range(start1-1,end1-1):
  timeline[i] += 1
#debugging
#print(timeline)
for i in range (start2-1,end2-1):
  timeline[i] += 1
#debugging
#print(timeline)
for i in range (start3-1,end3-1):
  timeline[i] += 1
#print(timeline)

cost = 0
for i in timeline:
  if i == 0: continue
  elif i == 1: cost += price1
  elif i == 2: cost += price2 * 2
  elif i == 3: cost += price3 * 3

print(cost)