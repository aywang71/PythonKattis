#https://open.kattis.com/problems/gerrymandering

#math.ceil needed
import math

#function to find the wasted votes in a district
def waste (sum_A,sum_B):
  # if function to find the party which wins
  # makes 3 variables: party which won, party-a wasted, and party-b wasted
  if (sum_A > sum_B): #Party A has won
    f = 'A'
    #formula here rounds up on the waste votes for party A's victory
    a = math.ceil(sum_A - ((sum_A + sum_B)/2 + 1))
    b = sum_B
  else: #Party B has won
    f = 'B'
    a = sum_A
    b = math.ceil(sum_B - ((sum_A + sum_B)/2 + 1))
  #returns as list
  return [f,str(a),str(b)]


#input form for iteration
p, d = input().split(' ')
p = int(p)
d = int(d)
#makes a list to compile all precincts
complier = []
#compiles blank list for each precinct
for x in range (d):
  complier.append([])
#debugging
#print(complier)

#goes through to input data values for p
for i in range (p):
  # takes in precinct data
  temp = [int(i) for i in input().split(' ')]
  #debugging
  #print('p:',temp)
  complier[temp[0]-1].append(temp[1:])
#debugging
#print('complier:',complier)

#makes a list for output 
output = []
#starts counting total voters
total = 0
#for each district
for i in complier:
  #debugging
  #print('district:',i)
  #resets the sums so each district's totals can be different
  sum_A = 0
  sum_B = 0
  #for each precinct
  for x in range(len(i)):
    #next 3 lines update values
    sum_A += i[x][0] 
    sum_B += i[x][1]
  total += sum_A + sum_B
  #runs values through function and adds to output list
  output.append(waste(sum_A,sum_B))
  #debugging
  #print('output',output)

#to calculate the efficency error
A = 0
B = 0
for i in output:
  #output
  print(' '.join(i))
  A += int(i[1])
  B += int(i[2])
#debugging
#print('values:',A,B,A+B)
#output
print(abs(A - B)/(total))