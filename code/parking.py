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
print(timeline)
for i in range (start2-1,end2-1):
  timeline[i] += 1
#debugging
print(timeline)
for i in range (start3-1,end3-1):
  timeline[i] += 1
count =0 
count1 = 0
count2 = 0
count3 = 0
#debugging
print(timeline)

#replaces the trucks per minute with costs
for i in range (0,len(timeline)):
  if timeline[i] == 1:
    timeline[i] = price1
  elif timeline[i] == 2:
    timeline[i] = price2
  elif timeline[i] == 3:
    timeline[i] = price3
  
#goes through to calculate costs
for i in range (0,len(timeline)):
  if i +1== end1:
    count += count1
    #debugging
    print('truck 1:',count1)
  elif (i + 1 <end1) and (i + 1 >=start1):
    count1 += timeline[i]
  if i +1== end2:
    count += count2
    #debugging
    print('truck 2:',count2)
  elif (i + 1 <end2) and (i + 1 >=start2):
    count2 += timeline[i]
  if i +1== end3:
    count += count3
    #debugging
    print('truck 3:',count3)
  elif (i + 1 <end3) and (i + 1 >=start3):
    count3 += timeline[i]
#output format
print(count)