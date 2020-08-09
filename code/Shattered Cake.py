#https://open.kattis.com/problems/shatteredcake

#to read entire input file at once
import sys
y = sys.stdin.read().split()
area = 0
#goe through each piece and adds it to area
for i in range (2,len(y),2):
  area += int(y[i]) * int(y[i+1])
#output
print(area//int(y[0]))