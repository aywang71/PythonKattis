#https://open.kattis.com/problems/platforme

n = int(input())

platforms = []
beams = []

for i in range(n):
  plat = [float(i) for i in input().split(' ')]
  platforms.append(plat)
  beams.append([plat[0],plat[0]]) #sets default as two beams of y height

platforms.sort(key = lambda x: x[0])

for i in range(n):
  #print('new platform: ', i + 1)
  #we want to find the intercepts:
  #finding left height first:
  left = platforms[i][1] + 0.5
  for x in range (i - 1,-1,-1):
    if (platforms[x][1] < left) and (platforms[x][2] > left):
      beams[i][0] -= platforms[x][0]
      #print('left beam stopped by platform: ', x + 1, 'new height: ', beams[i][0])
      break
  #check the right beam
  right = platforms[i][2] - 0.5
  for j in range (i - 1,-1,-1):
    if (platforms[j][1] < right) and (platforms[j][2] > right):
      #print(platforms[j][2], ' > ', right)
      beams[i][1] -= platforms[j][0]
      #print('right beam stopped by platform: ', j + 1, 'new height: ', beams[i][1])
      break
  
#print(beams)
print(int(sum([sum(i) for i in beams])))