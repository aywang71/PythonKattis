#https://open.kattis.com/problems/heliocentric

#needs sys for EOF reading
import sys

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
  #output
  print("Case",str(count)+':',str(out))

