#https://open.kattis.com/problems/greedypolygons

import math # need pi

n = int(input())

for i in range(n):
  sides, length, dist, grabs = input().split(' ')
  sides = int(sides)
  length = int(length)
  dist = int(dist)
  grabs = int(grabs)

  #calculate rectanglar area for grabs
  rectangle = dist * length #calculate the area of the rectangle produced
  rectArea = rectangle * sides  * grabs #combines the rectangles into a total rectangular area
  #print(f"Rectangle area: {rectArea}")

  #calculate arc area
  innerAngle = (sides - 2) * 180 / sides
  innerRadian = math.radians(innerAngle)
  #print(f"Inner angle: {innerAngle}")
  arcAngle = 180 - innerAngle
  #print(f"Arc angle: {arcAngle}")
  radius = dist * grabs 
  arcRadian = math.radians(arcAngle)
  arcArea = (radius ** 2) * arcRadian * sides * 0.5
  #print(f"Arc area: {arcArea}")

  #calculate base polygon area: wrong?
  baseArea = sides * length * 0.5 * (math.tan(innerRadian/2) * length * 0.5)
  #print(f"Base area: {baseArea}")

  print(rectArea + baseArea + arcArea)

  #print(' ------------------------------------------- ')