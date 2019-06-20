#https://open.kattis.com/problems/alphabetspam
#input format
string = input()
#storage values
white_space = 0
upper_case = 0
lower_case = 0
symbols = 0
#for each character you checks its parameters as whitespace, upper, lower, or symbol
for i in string:
  if i == '_':
    white_space += 1
  elif i.islower():
    upper_case+= 1
  elif i.isupper():
    lower_case+=1
  else:
    symbols += 1

#debugging
print(white_space)
#debugging
print(upper_case)
#debugging
print(lower_case)
#debugging
print(symbols)
#debugging
print(len(string))

#output format
print(white_space/len(string))
print(upper_case/len(string))
print(lower_case/len(string))
print(symbols/len(string))
