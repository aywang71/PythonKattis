#https://open.kattis.com/problems/isithalloween
n = input().split()
  # Another prime example of debugging
  print(n)
# A simple if statement to check values of list n for inputs
if n[0] == 'OCT' and n[1] == '31':
  print('yup')
elif n[0] == 'DEC' and n[1] == '25':
  print('yup')
else:
  print('nope')


