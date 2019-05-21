#https://open.kattis.com/problems/bijele
#list of correct values for future reference
correct = [1,1,2,2,2,8]
#splits input based on spaces
n = input().split(' ')
#creates a list to store difference
fix =[]
#for loop which solves difference between correct[] and n[]; stored in fix
for i in range (0,len(n)):
  n[i] = int(n[i])
  fix.append(correct[i]-n[i])
#DEBUGGIN
#Prints out correct, n, and fix row by row to see which correct OOO
print(correct)
print(n)
print(fix)
#Another for statment to convert statements in fix[] to str; this is for the join statement
for i in range (0,len(fix)):
  fix[i]=str(fix[i])
#debugging
print(fix)
#output
print(' '.join(fix))

