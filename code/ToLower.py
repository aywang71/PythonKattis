#https://open.kattis.com/problems/tolower

#iteration inptus
p, t = input().split(' ')
p = int(p)
t = int(t)
count = 0
#iteration loop for problems
for i in range (0,p):
  #resets passed tests
  tests = 0
  #iteration loop for test cases per problem
  for x in range (0,t):
    #string input
    string = input()
    #checks for lowercase
    for x in range (1,len(string)):
      if string[x].islower():
        continue
      else:
        #if there is an uppercase, substract 1 from tests passed
        tests -= 1
        break
    # automatically adds 1, but if not passed it stays same
    tests += 1
  #adds integer floor divide
  count += (tests//t)
#output 
print(count)