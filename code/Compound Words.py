#https://open.kattis.com/problems/compoundwords

#to read EOF
import sys
#possible word segments
words =[]

#input format
for line in sys.stdin:
  word = line.strip()
  word = word.split(' ')
  #debugging
  print(word)
  for i in word:
    words.append(i)

#normal input
'''
for i in range (0,2):
  word = input().split(' ')
  if word == '0':
    break
  else:
    for i in word:
      words.append(i)
'''
#debugging
print(words)
#future output stuff
output = []
#nested for to permutation it
for i in words:
  for x in words:
    if i == x:
      continue
    #concatinates word
    temp = i + x
    # adds to output
    output.append(temp)
#formats output
output = list(set(output))
output = sorted(output)
#debugging
print(output)
#output 
for i in output:
  print(i)
