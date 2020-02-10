#https://open.kattis.com/problems/simonsays

#iteration input
n = int(input())
for i in range (0,n):
  #further input for simon string order
  string = input().split(' ')
  #if and output
  if string[0] == "Simon" and string[1]=="says":
    print(' '.join(string[2:]))