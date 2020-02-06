#https://open.kattis.com/problems/dicegame

#inputs on dice and data conversion
amin1,amax1,amin2,amax2 = input().split(' ')
amin1 = int(amin1)
amax1 = int(amax1)
amin2 = int(amin2)
amax2 = int(amax2)
bmin1,bmax1,bmin2,bmax2 = input().split(' ')
bmin1 = int(bmin1)
bmax1 = int(bmax1)
bmin2 = int(bmin2)
bmax2 = int(bmax2)
#finds averages and total
adie1 = (amin1+amax1)/2
adie2 = (amin2+amax2)/2
bdie1 = (bmin1+bmax1)/2
bdie2 = (bmin2+bmax2)/2
atotal = adie1+adie2
btotal = bdie1+bdie2
#if function for output
if atotal > btotal:
  print('Gunnar')
elif btotal>atotal:
  print('Emma')
elif btotal==atotal:
  print('Tie')