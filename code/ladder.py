#https://open.kattis.com/problems/ladder
#gives us math functions
import math 
# splits variables based on ' '
h, v = input().split()
#confirms integer values
h = int(h)
v = int(v)
#converts degrees to radians
v = math.radians(v)
# new variable for the sin of radians
sin = math.sin(v)
#height is h/sin
height = h/sin
#prints the height rounded to nearest integer
print(math.ceil(height))
