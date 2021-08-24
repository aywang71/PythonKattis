#https://open.kattis.com/problems/yinyangstones

#gets input
stones = list(input())
#if unequal there is no way to make equal
if stones.count('W')!= stones.count('B'):
  print('0')
else:
  #if equal, you can do it 
  print('1')
