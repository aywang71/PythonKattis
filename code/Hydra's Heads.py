#https://open.kattis.com/problems/hydrasheads

# Inputs for head and tail until head tail == 0
while True:
  #split and conversion to integer
  head,tail = input().split(' ')
  head = int(head)
  tail = int(tail)
  #resets count to 0 
  count = 0
  #posttest loop if head and tail == 0
  if head == 0 and tail == 0:
    break
  else:
    
    while True:
      if (head == 0) and (tail == 0):
        print(count)
        #print('heads:%i tails: %i; succeed' %(head,tail))
        break
      elif head>1:
        head -= 2
        count +=1
        #print('heads:%i tails: %i' %(head,tail))
      elif (tail >1 and head!=0) or tail>=4:
        tail -=2
        head += 1
        count+= 1
        #print('heads:%i tails: %i' %(head,tail))
      elif tail<4:
        tail += 1
        count += 1
        #print('heads:%i tails: %i' %(head,tail))
      else:
        print('-1')
        #print('heads:%i tails: %i; fail' %(head,tail))
        break
    #print('heads:%i tails: %i; break' %(head,tail))
  #print(count)

