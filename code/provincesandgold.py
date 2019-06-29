#https://open.kattis.com/problems/provincesandgold
#input format
gold,silver,copper = input().split(' ')
#conversions to proper data type
gold = int(gold)*3
#debugging
print(gold)
silver = int(silver)*2
#debugging
print(silver)
copper = int(copper)
#debugging
print(copper)

# storage values
buy_power = gold+ silver + copper
#debugging
print(buy_power)
victory_cards = [2,5,8]
#debugging
print(victory_cards)
victory_names = ["Estate","Duchy","Province"]
#debugging
print(victory_names)
victory_index = -1
treasure_cards = [0,3,6]
#debugging
print(treasure_cards)
treasure_names = ["Copper","Silver","Gold"]
#debugging
print(treasure_names)
treasure_index = 0

#very complex if statement for getting values of buy_power
if buy_power>=8:
  victory_index = 2
  treasure_index = 2
elif buy_power == 7:
  victory_index = 1
  treasure_index = 2
elif buy_power == 6:
  victory_index = 1
  treasure_index = 2
elif buy_power == 5:
  victory_index = 1
  treasure_index = 1
elif buy_power == 4:
  victory_index = 0
  treasure_index = 1
elif buy_power == 3:
  victory_index = 0
  treasure_index = 1
elif buy_power == 2:
  victory_index =0
  treasure_index = 0

#output format 
if victory_index == -1:
  print(treasure_names[treasure_index])
else:
  print('%s or %s'%(victory_names[victory_index],treasure_names[treasure_index]))




#broken code enter at your own risk:
  '''
for i in range (0,3):
  if buy_power>=victory_cards[i]:
    if i == 2:
      victory_index = 2
    continue 
  else :
    if i == 0:
      break
    else: 
      victory_index = i -1
  break  
print(victory_index)

for i in range (0,3):
  if buy_power >= treasure_cards[i]:
    if i ==2:
      victory_index = 2
    continue
  else:
    if i == 0:
      break
    else:
      treasure_index = i -1
  break
print(treasure_index)
'''
