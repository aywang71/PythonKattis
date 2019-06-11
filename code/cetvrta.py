#https://open.kattis.com/problems/cetvrta

#input format for coordinates
point1 = input().split(' ')
point2 = input().split(' ')
point3 = input().split(' ')
#creates a list for x and y values
point_x= [] 
point_y= []
#appends x values to x list
point_x.append(point1[0])
point_x.append(point2[0])
point_x.append(point3[0])
#appends y values to y list
point_y.append(point1[1])
point_y.append(point2[1])
point_y.append(point3[1])
# creates 2 str variables for coordinate storage
point_output_x = '0'
point_output_y = '0'
#debugging to view list
print(point_x)
print(point_y)
# for loop for anything in x/y list
for i in range (0,len(point_x)):
  # if there is 2 of the same coordinate (which there must be as a property of rectangles), take the thrid one
  if point_x.count(point_x[i]) == 1:
    point_output_x = point_x[i]
  if point_y.count(point_y[i]) == 1:
    point_output_y = point_y[i]
#formats output
print(point_output_x + ' ' + point_output_y)


