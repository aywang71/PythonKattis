#https://open.kattis.com/problems/speeding

n = []
maxi = 0

for i in range(int(input())):
  point = input().split(' ')
  point[0] = int(point[0])
  point[1] = int(point[1])

  n.append(point)

#print(n)

for i in range(1, len(n)):
  if int((n[i][1] - n[i-1][1]) / (n[i][0] - n[i-1][0])) > maxi: maxi = int((n[i][1] - n[i-1][1]) / (n[i][0] - n[i-1][0])) 

print(maxi)
