#https://open.kattis.com/problems/skener

#input
base_rows,base_characters,mod_rows,mod_char = input().split(' ')
base_characters = int(base_characters)
mod_char = int(mod_char)
mod_rows = int(mod_rows)
#matrix's for processing
matrix = []
test_matrix = []
final_matrix = []
#further inputs
for i in range (0,int(base_rows)):
  row = list(input())
  matrix.append(row)
#debugging
print(matrix)
print(len(matrix))
#adjusts horizontal
for m in range (0,len(matrix)):
  #resets row every row
  row = []
  #appends the number of requested characters per row
  for i in range (0,base_characters):
    for x in range (0,mod_char):
      row.append(matrix[m][i])
  test_matrix.append(row)
#deubgging
print(test_matrix)
#adjusts veritcal
for m in range (0,len(test_matrix)):
  for i in range (0,mod_rows):
    final_matrix.append(test_matrix[m])
#print(final_matrix)
for x in range (0,len(final_matrix)):
  print(''.join(final_matrix[x]))