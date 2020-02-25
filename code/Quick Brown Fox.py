#https://open.kattis.com/problems/quickbrownfox

#iteration input
n = int(input())
for i in range (0,n):
  #resets pangram coutner per iteration
  alphabet = list('abcdefghijklmnopqrstuvwxyz')
  #more inputs
  check = list(input())
  for i in range (0,len(check)):
    #checks if letter
    try:
      #debugging
      print(check[i].lower())
      #don't want to remove it if its already removed
      if check[i].lower() in alphabet:
        alphabet.remove(check[i].lower())
      #debugging
      print(alphabet)
    except:
      pass
  #output format
  if len(alphabet) == 0:
    print('pangram')
  else:
    print('missing',''.join(alphabet))
