#https://open.kattis.com/contests/qm8axp/problems/pizza

#range iterator
test_cases = int(input())
for case in range(test_cases):
  # inputs for the columns and rows
  cols, rows = input().split(' ')
  #to integer
  rows = int(rows)
  cols = int(cols)
  #resets the city virtual grid
  city = []
  #gets rows into the city
  for i in range (rows):
    city.append([int(i) for i in input().split(' ')])
  #resets the sum vars
  rows_sum = []
  cols_sum = []
  # adds the sum of each row to the rows_sum
  for i in range(rows):
    rows_sum.append(sum(city[i]))
  #same as above but for columns
  for i in range(cols):
    x = 0
    for g in range(rows):
      #debugging
      #print(g, i,' debug')
      x += city[g][i]
    cols_sum.append(x)
  act_rows_sum = []
  act_cols_sum = []
  for i in range(0, len(rows_sum)):
    act_rows_sum.append(0)
    for g in range(0, len(rows_sum)):
      act_rows_sum[i] += abs(g-i)*rows_sum[g]
  for i in range(0, len(cols_sum)):
    act_cols_sum.append(0)
    for g in range(0, len(cols_sum)):
      act_cols_sum[i] += abs(g-i)*cols_sum[g]
  z = min(act_cols_sum) + min(act_rows_sum)
  print(str(z) + ' blocks')