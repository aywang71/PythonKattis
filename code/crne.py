#https://open.kattis.com/problems/crne

#in this problem you need to find the most square cuts
x = int(input(''))
#integer divides to evenly split
y = x//2
#debugging
#print(y)
#resets x value
x =  x-y
#debugging
#print(x)
#output
print((x+1)*(y+1))