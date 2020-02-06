#https://open.kattis.com/problems/mixedfractions

#runs until:
while True:
  #input
  numerator, denominator = input().split()
  numerator = int(numerator)
  denominator = int(denominator)\
  #break condition
  if numerator == 0 and denominator == 0:
    break
  else:
    #wholes anf fraction portions
    whole = numerator//denominator
    fraction = numerator%denominator
    #debugging
    print(whole)
    print(fraction)
    #output format
    print('%i %i / %i'%(whole,fraction,denominator))