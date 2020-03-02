#https://open.kattis.com/problems/tetration

#input
n = float(input())
#formula to solve infinite tetration
a = n ** (1/n)
#output
print(a)