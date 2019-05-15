#https://open.kattis.com/problems/conundrum
n = list(input())
days = 0

#This range must be from 0 to len(n)-1 since array numeric values begin at 0
for i in range (0,len(n)):
  #converts each value to a string
  n[i] = str(n[i])
 
  #IMPORTANT
  #Use case example of breakpoints/debugging
  print("i=" + str(i) + ", n[i]" + n[i]);
  
  # serires of if statements to check for the character value in a specific array value. We need to use % so that we cement the order of the characters. 
  if i%3 == 0 and n[i] is "P":
    days=days
  elif i%3 == 1 and n[i] is "E":
    days = days
  elif i%3 == 2 and n[i] is "R":
    days = days
  else:
    days +=1

print(days)




