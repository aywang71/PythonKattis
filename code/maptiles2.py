#https://open.kattis.com/problems/maptiles2
#input
quadkey = list(input())
#finds length of grid
size = int((4**(len(quadkey)))**0.5)
#topleft and bottomright corners
topleft = [0,0]
bottomright = [size-1,size-1]
#goes throught to alter the coordinates
for i in quadkey:
  size //=2
  #alters the topleft 
  if i == '1':
    topleft = [(topleft[0]+bottomright[0])//2+1,topleft[1]]
  elif i == '2':
    topleft = [topleft[0],(topleft[1]+bottomright[1])//2+1]
  elif i == '3':
    topleft = [(topleft[0]+bottomright[0])//2+1,(topleft[1]+bottomright[1])//2+1]
  bottomright = [topleft[0]+size-1,topleft[1]+size-1]
  #debugging
  print('size:',size)
  print('topleft:',topleft)
  print('bottomright:',bottomright)
#output
print(len(quadkey),topleft[0],topleft[1])