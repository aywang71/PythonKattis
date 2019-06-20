#https://open.kattis.com/problems/railroad2
#input for junctions and switches
junction,switch = input().split(' ')
#this means that each junction can support 4 tracks, while each switch supports 3 tracks
junction = 4*int(junction)
switch = 3*int(switch)
#total tracks
tracks = junction + switch
#if there is an odd number of tracks its impossible
if tracks%2 ==0:
  print('possible')
else:
  print('impossible')
