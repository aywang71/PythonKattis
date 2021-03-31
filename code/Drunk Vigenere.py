#https://open.kattis.com/problems/drunkvigenere

message = list(input())
key = list(input())
alphabet = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
out = []

for i in range (len(message)):
  shift = alphabet.index(key[i])
  if i % 2 == 0:
    #shift += alphabet.index(message[i])
    shift = alphabet.index(message[i]) - shift
  else: 
    #shift = alphabet.index(message[i]) - shift
    shift += alphabet.index(message[i])
  shift = shift % 26
  print(f'shift{shift}')
  out.append(alphabet[shift])

print(''.join(out))
