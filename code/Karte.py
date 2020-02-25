#https://open.kattis.com/problems/karte

#input format
string = input()
#storage 
cards = []
suits = [13,13,13,13]
i = 0
#splits input into cards
while i <len(string):
  i += 3
  x = string[i-3:i]
  #debugging
  print(x)
  cards.append(x)
#debugging
print(cards)
#boolean to continue
cont = True
# sees for repeats
for i in range (0,len(cards)):
  if cards.count(cards[i]) >1:
    print('GRESKA')
    cont = False
    break
#output format
if cont == True:
  big = list(''.join(cards))
  suits[0] = str(suits[0] - big.count('P'))
  suits[1] = str(suits[1] - big.count('K'))
  suits[2] = str(suits[2] - big.count('H'))
  suits[3] = str(suits[3] - big.count('T'))
  print(' '.join(suits))
