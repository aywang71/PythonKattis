#https://open.kattis.com/problems/drmmessages

#inputs a string
string = list(input())
#debugging
print(len(string))
#lists for splitting, alphabet, and drift amount
first_half = []
second_half = []
letter_drift = 0
alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

#seperates string into first and second halves
for i in range (0,int(len(string)/2)):
  first_half.append(string[i])
  second_half.append(string[i+int(len(string)/2)])
#debugging
print(first_half)
print(second_half)
#finds letter drift for first half
for i in range (0,len(first_half)):
  x= alphabet.index(first_half[i])
  letter_drift += x
#debugging
print(letter_drift)
#sets each value in first half to a new drifted value
for i in range (0,len(first_half)):
  first_half[i] = alphabet[(alphabet.index(first_half[i])+letter_drift)%len(alphabet)]
#debugging
print(first_half)
letter_drift = 0
#finds letter drift for second half
for i in range (0,len(second_half)):
  x= alphabet.index(second_half[i])
  letter_drift += x
#debugging
print(letter_drift)
#sets each value in second half to a new drifted value
for i in range (0,len(second_half)):
  second_half[i] = alphabet[(alphabet.index(second_half[i])+letter_drift)%len(alphabet)]
#debugging
print(second_half)
#changes values in first half by its difference in the second half
for i in range (0,len(first_half)):
  x = alphabet.index(second_half[i])
  y = alphabet.index(first_half[i])
  first_half[i] = alphabet[(x+y)%len(alphabet)]
#debugging
print(first_half)
#output
print(''.join(first_half))