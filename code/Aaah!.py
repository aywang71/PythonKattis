#https://open.kattis.com/problems/aaah

#what the person can give
give = list(input())
#debugging
print(give)
give.remove('h')
#what the doctor needs
need = list(input())
need.remove('h')
#basically it needs how long he can say "aaah" for, so take length
if len(give) <len(need):
  print('no')
else:
  print('go')