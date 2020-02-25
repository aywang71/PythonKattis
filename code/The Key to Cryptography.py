#https://open.kattis.com/problems/keytocrypto

#for index reference
alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
#input
coded = list(input())
uncoded = list(input())
output = []
item = 0
#until everything is uncoded
while item != len(coded):
  #finds shift through subtraction, since its decoding
  shift = (alphabet.index(coded[item]) - alphabet.index(uncoded[item]))%26
  #debugging
  print('shift:',shift)
  print('letter:',alphabet[shift])
  #appends
  uncoded.append(alphabet[shift])
  output.append(alphabet[shift])
  item += 1
#output
print(''.join(output))