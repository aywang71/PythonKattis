#https://open.kattis.com/problems/detaileddifferences
# the goal here is to compare different strings and each character in that string
n = int(input())
difference_count = []
# to store the string-list variations
storage_tot_input1 = []
storage_tot_input2 = []
for i in range (0,n):
  first_input= list(input())
  second_input= list(input())
  storage_tot_input1.append(first_input)
  storage_tot_input2.append(second_input)
  control_tot = []
  for i in range (0,len(first_input)):
    if first_input[i] == second_input[i]:
      control_tot.append(".")
    else:
      control_tot.append("*")
  difference_count.append(control_tot)

#print(difference_count)
for i in range(0,n):
  if i==n*2:
    continue
  else:
      input_one_disp = ''.join(storage_tot_input1[i])
      print(input_one_disp)
      input_two_disp = ''.join(storage_tot_input2[i])
      print(input_two_disp)
  difference_count_disp=''.join(difference_count[i])
  print(difference_count_disp)
  print('')
