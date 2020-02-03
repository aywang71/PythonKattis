#https://open.kattis.com/problems/herman

#brings in math library
import math
#input for radius size
n= int(input())
#normal area
e_area = math.pi *n * n
print(e_area)

# a taxicab circle is a square, and its diagonals are 2r, therefore its size lengths are sqrt(2rr)
t_area = 2*n*n
print(t_area)