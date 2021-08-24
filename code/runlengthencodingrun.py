#https://open.kattis.com/problems/runlengthencodingrun

#encoding function
def encode ( string ):
  string = list(string)
  encoded = []
  count = 1
  for char in range (0,len(string)-1):
    #debugging
    print(string[char])
    if string[char] == string[char+1]:
      count += 1
      continue
    else:
      encoded.append(string[char])
      encoded.append(str(count))
      count = 1
  encoded.append(string[len(string)-1])
  encoded.append(str(count))
  print(''.join(encoded))
  return

#decoding function
def decode ( string ):
  string = list(string)
  decoded = []
  for char in range (0,len(string)-1,2):
    string[char+1] = int(string[char+1])
    for x in range (0,string[char+1]):
      decoded.append(string[char])
  print(''.join(decoded))
  return

#input
settup, string = input().split(' ')
#output
if settup == "E":
  encode(string);
elif settup == "D":
  decode(string)



