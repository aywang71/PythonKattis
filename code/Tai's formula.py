#https://open.kattis.com/problems/taisformula

# iteration input
n = int(input())
#sorting
times = []
glucoses = []
total = 0
for i in range (0,n):
  #more input
  time, glucose = input().split(' ')
  time = int(time)
  glucose = float(glucose)
  #sort to lists
  times.append(time)
  glucoses.append(glucose)
# finds area of triangles in the graph
for x in range (1,n):
  time1 = times[x-1]
  glucose1 = glucoses[x-1]
  time2 = times[x]
  glucose2 = glucoses[x]
  differenceg = abs(glucose2-glucose1)
  differencet = abs(time2-time1)
  rectangle = differencet * min(glucose1,glucose2)
  triangle = differenceg * differencet *0.5
  #debugging
  print(rectangle)
  print(triangle)
  total += rectangle + triangle
  #debugging
  print(total)
#output
print(total/1000)
