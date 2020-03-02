#https://open.kattis.com/problems/quiteaproblem

#sys for EOF read in
import sys
for line in sys.stdin:
  #simple if/else
  if 'problem' in line.lower():
    print('yes')
  else:
    print('no')
#traditional input formats
'''
n = int(input())
for i in range (n):
  string = input()
  if 'problem' in string.lower():
    print('yes')
  else:
    print('no')
'''
