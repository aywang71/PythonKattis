#https://open.kattis.com/problems/inflation

#number of balloons
n = int(input())
#Gases per container bought and integer
gas = (int(x) for x in input().split(' '))
#makes lists for baloons, sums, and ratios
balloons = []
sums = []
ratios =[]
#sorts gas from least to greatest
gas = sorted(gas)


for i in range (n):
  balloons.append(i+1)
  #appends to sums list how much space each balloon has left
  sums.append(balloons[i]-gas[i])

#goes through to check if any balloons are overfilled, and fixes them
#more debugging
#print('balloons:',balloons)
#print('gas:',gas)
#print('sums:',sums)
#print('ratios:',ratios)

#ending boolean
cont = True
#goes through to find something less than 0
for i in range (0,len(sums)):
  if sums[i]<0:
    #will either print 0, if gas canister re-routed, or impossible
    try:
      choosen = min(filter(lambda x : x >= gas[i], sums))
      print('0')
    except:
      print('impossible')
    cont = False
    break
#follows up booleans
if cont == True:
  #does ratios
  for i in range (n):
    ratios.append((balloons[i]-sums[i])/balloons[i])
  #outputs
  print(min(ratios))
  


