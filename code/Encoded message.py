#https://open.kattis.com/problems/encodedmessage

#needed for square root 
import math
#number of iterations
n= int(input())
for i in range (0,n):
  #list input
  string = list(input())
  #debugging
  print(len(string))
  count = 0
  decoded = []
  interval = math.sqrt(len(string))
  character_number = -1
  floor_character = 0
  #runs until iterations is larger than length
  while count < len(string):\
    #does calculations to find next character
    character_number+= interval
    previous_floor_character = floor_character
    floor_character = character_number//len(string)
    if floor_character != previous_floor_character:
      character_number-=1
    #debugging
    print(character_number%len(string))
    decoded.append(string[int(character_number%len(string))])
    count += 1
  #debugging
  print(''.join(decoded))