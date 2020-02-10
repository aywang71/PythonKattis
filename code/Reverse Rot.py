#https://open.kattis.com/problems/reverserot

#alphabet for shifting
alphabet = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ_.')
#debugging
print(alphabet)
#until input 0
while True:
  #inputs
  input1= input().split(' ')
  shift = int(input1[0])
  if shift == 0:
    break
  string = list(input1[1])
  #debugging
  print(string)
  #changes values via shift
  for i in range (0,len(string)):
    #debugging
    print(alphabet.index(string[i])+shift)
    #shift function
    string[i] = alphabet[(alphabet.index(string[i])+shift)%28]
  #debugging
  print(string)
  #reverse
  string = string[::-1]
  #debugging
  print(string)
  #output
  print(''.join(string))
