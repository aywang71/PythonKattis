#https://open.kattis.com/problems/mosquito

#sys for eof reading
import sys
#copy for deepcopy
import copy
#goes through each line in input
for line in sys.stdin:
  #input
  data = [int(x) for x in line.split()]
  #makes two lists, as one is needed to look back on
  data2 = [data[2],data[1],data[0]]
  new = [0,0,0]
  #debugging
  print(data)
  #does the calculations
  for i in range (0,data[-1]):
    #debugging
    print('stats begin:',data2)
    new[0] = data2[2]*data[3]
    #debugging
    print('stats break 1:',data2)
    new[1] = data2[0]//data[4]
    new[2] = data2[1]//data[5]
    data2 = copy.deepcopy(new)
    #debugging
    print('stats:',data2)
  #output
  print(data2[2])


