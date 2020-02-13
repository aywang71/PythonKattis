#https://open.kattis.com/problems/heliocentric

#needs sys for EOF reading
import sys

#earth: 365 | mars: 687

#TODO: find lcm with mods (based on input)
count = 0
#input
for line in sys.stdin:
  count += 1
  # variable inputs
  earth,mars = line.split(" ")
  earth = int(earth)
  mars = int(mars)
  out = 0
  # as long as earth and mars do not equal 0
  while earth != mars:
    #increment
    earth += 1
    mars += 1
    if mars >= 687:
      mars = 0
    if earth >= 365:
      earth = 0
    out += 1
    #debugging
    print('iteration:',earth,mars) 
  #output
  print("Case",str(count)+':',str(out))

