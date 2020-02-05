#https://open.kattis.com/problems/hangingout

#inputs and formatting
max_people, number_groups = input().split(' ')
max_people = int(max_people)
number_groups = int(number_groups)
#variables for total and banned groups
total = 0
count = 0
#gets number_group inputs of groups
for i in range (0,number_groups):
  #input and formatting
  status, amount = input().split(' ')
  amount = int(amount)
  #complex if statement to check for validation
  if status == "enter":
    if (total + amount) > max_people:
      count += 1
      #print(total)
      continue
    else:
      total += amount
      #print(total)
  else:
    total -= amount
    #print(total)
print(count)