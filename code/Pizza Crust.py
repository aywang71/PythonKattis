#https://open.kattis.com/problems/pizza2

#import math library
import math
#inputs for radius and crust
radius, crust = input().split(' ')
radius = int(radius)
crust = int(crust)
#area and nonarea
pizza_area = math.pi * radius*radius
noncrust_area = math.pi *(radius-crust) *(radius-crust)
#output format
print(noncrust_area/pizza_area*100)

