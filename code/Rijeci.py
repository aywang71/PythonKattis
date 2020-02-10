#https://open.kattis.com/problems/rijeci

#iteration input
n = int(input())
#for sums a,b and fibannoci of a and b
a= 0
fibA = [0,1]
b= 0
fibB = [1,1]
#we can't do it for the first two iterations
show = True
if n == 1:
  print('0 1')
  show = False
elif n==2:
  print('1 1')
  show = False
if show == True:
  #starts at iteration 3
  for i in range (2,n):
    #the sum is the addition of the last two terms 
    a = sum(fibA)
    b = sum(fibB)
    #now the second-to-last term is last iterations term and the current turn's term is a/b
    fibB[0] = fibB[1]
    fibB[1] = b
    fibA[0] = fibA[1]
    fibA[1] = a
    #debugging
    print('A:',fibA)
    print('B:',fibB)
  #output
  print('%i %i'%(a,b))

'''
  a = string.count('a')
  b = string.count('b')
  for i in range (0,b):
    string.append('a')
    string.append('b')
    string.remove('b')
  for i in range (0,a):
    string.append('b')
    string.remove('a')
  #print(string)
print('%i %i'%(a,b))
'''