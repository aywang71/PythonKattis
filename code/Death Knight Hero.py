#https://open.kattis.com/problems/deathknight

#count variable for success
count = 0
#number of input iterations
n = int(input())
for i in range (0,n):
  #string list inputs
  string = input()
  #looks for CD
  if "CD" in string:
    continue
  else:
    count+= 1
#output
print(count)