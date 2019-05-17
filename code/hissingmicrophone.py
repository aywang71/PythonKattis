#https://open.kattis.com/problems/hissingmicrophone
#list input
n = list(input())
#variable to set as 1
x = 0
# for loop in each character of the list up to the 2nd to last
for i in range (0,len(n)-1):
  #conversion to string
  n[i]=str(n[i])
  #if statement for checking s in consecutive
  # note that this will only run once, as the second time x=1
  if n[i] is "s" and  n[i+1]is"s"and x!= 1:
    print("hiss")
    x=1
    #debug portion
    print("n[",i,"]", "is s and n[",i+1,"] is also s")
  else:
    #if its not correct keep going
    continue
#if nothing in the if statment is true, there is no hiss
if x!=1:
  print("no hiss")


     
