#https://open.kattis.com/problems/cudoviste

#alternate input
#rows, columns = [int(x) for x in input().split()]
#input formatting
rows, columns = input().split(" ")
rows = int(rows)
columns = int(columns)
#virtual grid
grid = []
# five counter variables
car0 = 0
car1 = 0
car2 = 0
car3 = 0
car4 = 0
#inpust for rows and makes virtual grid
for i in range (0,rows):
  row = list(input())
  grid.append(row)
#for the entire grid (but-1 for list indexing)
for i in range (0, rows - 1):
  for x in range (0, columns -1 ):
    #creates a temporary grid for the block of four
    temp_grid = [grid[i][x],grid[i][x+1],grid[i+1][x],grid[i+1][x+1]]
    #debugging
    print(temp_grid)
    #no buildings
    if "#" in temp_grid:
      continue
    else:
      #counts cars
      car_count = temp_grid.count("X")
      if car_count == 0:
        car0 += 1
        #debugging
        print('car0 = ',car0)
      elif car_count == 1:
        car1 += 1
        #debugging
        print('car1 = ',car1)
      elif car_count == 2:
        car2 += 1
        #debugging
        print('car2 = ',car2)
      elif car_count == 3:
        car3 += 1
        #debugging
        print('car3 = ',car3)
      elif car_count == 4:
        car4 += 1
        #debugging
        print('car4 = ',car4)
#output format
print(car0)
print(car1)
print(car2)
print(car3)
print(car4)