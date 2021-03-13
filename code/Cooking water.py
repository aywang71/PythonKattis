#https://open.kattis.com/problems/cookingwater

# makes sure that no starting value is after the ending value
def start_check(start,out):
  for i in start:
    if i > out[1]:
      #debugging
      #print(i,'>',out[1])
      return False
  return True

#makes sure that no ending value is before the starting value
def end_check(end,out):
  for i in end:
    if i < out[0]:
      #debugging
      #print(i,'<',out[0])
      return False
  return True

#iteration input
num = int(input(""))
#start and end times 
start = []
end = []
#gets num amount of start and end times
for i in range(0, num):
  a, b = input('').split(" ")
  a = int(a)
  b = int(b)
  #formats them into the list
  start.append(a)
  end.append(b)
#debugging
#print(start, end)
#creates a list with the latest starting time and earliest ending time
out = [max(start),min(end)]
#debugging
#print(out)

#if all these functions are ok: 
if (out[0] <= out[1]) and start_check(start, out) and end_check(end, out):
  #debugging
  #print('hi')
  #if the max starting time is > than the min ending time
  if out[0] > out[1]:
    #this would mean that not all pots boil at the same time
    print('edward is right')
  else:
    print('gunilla has a point')
#if there is an error in checking gunilla is correct
else:
  print('edward is right')