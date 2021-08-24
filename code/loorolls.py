#https://open.kattis.com/problems/loorolls

#input format
length, use = input().split(' ')
length = int(length)
use = int(use)
count = 0
cont = True
# if it goes in perfectly
if (length%use == 0):
  #debugging
  print('yes')
  if length >= use:
    #that means it goes in perfectly and only one roll will ever be used
    print(1)
  else:
    #debugging
    print(use/length)
    #more output for a double type number
    print(str(use/length)[0:-2])
  cont = False
#runs through first division
remain = use - (length%use)
#debugging
print('remain:',remain)
if cont == True:
  #until it 0s out
  while length%remain != 0:
    #formula to change the remain variable
    remain = remain - (length%remain)
    #debugging
    print('remain:',remain)
    count += 1
  #output
  print(count+2)
