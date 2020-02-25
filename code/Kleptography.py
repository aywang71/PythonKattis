#https://open.kattis.com/problems/kleptography

#makes a list to retreieve values
alphabet = list('abcdefghijklmnopqrstuvwxyz')
#input format
key, string = input().split(' ')
keyword = list(input())
encrypt = list(input())
#the output list
decrypt = []
#gets the amount of empty characters
for i in encrypt:
  decrypt.append(' ')
#makes the last key digits of decrypt the last keyword digits
for i in range(0,len(keyword)):
  decrypt[-i-1] = keyword[-i-1]
#count value
i = 0
#until decrypt is filled
while decrypt.count(' ') >0:
  #debugging
  print(decrypt)
  #finds the value to move
  x = (26 + alphabet.index(decrypt[-i-1]) - alphabet.index(encrypt[-i-1])) %26
  #moves counter one over
  i += 1
  #appends to decrypt
  decrypt[-i-len(keyword)] = alphabet[-x]
  #debugging
  print(x)
  print(alphabet[-x])
#output
print(''.join(decrypt))
  


