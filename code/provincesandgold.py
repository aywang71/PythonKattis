#https://open.kattis.com/problems/provincesandgold
#input format 
coins = [int(i) for i in input().split(' ')]
#print(coins)
power = coins[0] *3 + coins[1] *2 + coins[2]
#print(power)

if power >= 8:
  victory = "Province"
  treasure = "Gold"
elif power >= 6:
  victory = "Duchy"
  treasure = "Gold"
elif power >= 5:
  victory = "Duchy"
  treasure = "Silver"
elif power >= 3:
  victory = "Estate"
  treasure = "Silver"
elif power >= 2:
  victory = "Estate"
  treasure = "Copper"
else: 
  victory = ""
  treasure = "Copper"

if victory == "": print(treasure)
else: print(f"{victory} or {treasure}")