#https://open.kattis.com/problems/kemija08

#input
string = input()
#vowel dict
vowels = {'a','e','i','o','u'}
#i as a string char ref
i = 0
#output list
new = []
#for when i is < string
while i <len(string)
  new.append(string[i])
  #if i is in vowels, skip next two
  if string[i] in vowels:
    i += 2
  i += 1
#output format
print(''.join(new))


  