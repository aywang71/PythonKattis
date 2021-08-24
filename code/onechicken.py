#https://open.kattis.com/problems/onechicken

#input
people, chicken = input().split(' ')
people = int(people)
chicken = int(chicken)
#if statement for chicken>people or people>chicken
if people > chicken:
  #plural/possessive
  if people - chicken == 1:
    print('Dr. Chaz needs 1 more piece of chicken!')
  else:
    print('Dr. Chaz needs %i more pieces of chicken!'%(people-chicken))
else:
  #plural/possessive
  if chicken - people == 1:
    print('Dr. Chaz will have 1 piece of chicken left over!')
  else:
    print('Dr. Chaz will have %i pieces of chicken left over!'%(chicken-people))