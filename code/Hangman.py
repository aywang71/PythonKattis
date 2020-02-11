#https://open.kattis.com/problems/hangman

#stops when its at 10
count = 0
#input format
word = list(input())
char = list(input())
#runs through
for i in char:
  if i in word:
    #debugging
    print('before: ', word)
    #removes all instances of that character
    for x in range (0,word.count(i)):
      word.remove(i)
    #debugging
    print('after: ', word)
  #addds counts
  else:
    count += 1
    #debugging
    print('count:', count)
    #then the hangman is complete
    if count >=10:
      print('LOSE')
      break
  #when all the letters are guessed
  if len(word) == 0:
    print('WIN')
    break