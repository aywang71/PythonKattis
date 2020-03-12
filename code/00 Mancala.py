# view logic: https://docs.google.com/spreadsheets/d/1sSVYOY0rgoR3dRgl06Ct7zyi9Sxq2uhttfb6M7yz9O4/edit?usp=sharing

#https://open.kattis.com/problems/mancala

#function to decrement each value by 1 for a maxed out placement
def decrement(out,pos):
  for i in range (0,pos):
    out[i] -= 1
  print('decremented list:',out)
  return out

def add (out):
  count = 0
  while True:
    #replace out[count] + 1 with a sum function for momentum
    try:
      #TODO: fix second part of comparison
      if (sum(out[0:count+1]) + 1) > (len(out[0:(count+1)]+1)):
        count += 1
      else:
        out[count] = count + 1
        out = decrement(out,count)
        break
    except:
      #adds a maxed out value to the end if the overflow reaches max index
      out.append(len(out)+1)
      out = decrement(out,len(out)-1)
      break
  print('updated list:',out)
  return out

def find (balls):
  #needs that for running ifs
  out = [0]
  count = 0
  #TODO: until you have the correct number of balls
  while count != balls:
    

for i in range (int(input())):
  case, balls = input().split(' ')
  balls = int(balls)
  out = find(balls)