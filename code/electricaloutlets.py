#https://open.kattis.com/problems/electricaloutlets

for i in range(int(input())):
  outlets = [int(i) for i in input().split(' ')]
  outlets.pop(0)
  print(sum(outlets) - len(outlets) + 1)