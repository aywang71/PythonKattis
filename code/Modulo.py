#https://open.kattis.com/problems/modulo

#seperate remainder array
mods = []
#for 10 inputs
for i in range (0,10):
  number = int(input())
  #if its in there, don't do it
  if number%42 in mods:
    #debugging
    print(number%42,"was in our list")
    continue
  else:
    #debugging
    print(number%42 ,"was not in our list")
    mods.append(number%42)
#output format
print(len(mods))
