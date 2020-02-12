def reverse(entered):
  temp = ''
  for i in entered:
    if i.isupper():
      #debugging
      print(i,'is uppercase')
      temp += i.lower()
    else:
      #debugging
      print(i,'is lowercase')
      temp += i.upper()
  #debugging
  #print('string',temp)
  return temp

#https://open.kattis.com/problems/softpasswords
password = input()
entered = input()
numbers = ['0','1','2','3','4','5','6','7','8','9']
#test 1 --> if they are equal
if password == entered:
  #debugging
  print('test 1')
  print('Yes')
else:
  #test 2 --> if you can add something to the front 
  if (password[1:] == entered) and (password[0] in numbers):
    #debugging
    print('test 2')
    print('Yes') 
  else:
    #test 3 --> if you can add something to the end
    if (password[:-1] == entered) and (password[-1] in numbers):
      #debugging
      print('test 3')
      print('Yes')
    else:
      #test 4 --> Reverse case
      if reverse(entered) == password:
        #debugging
        print('test 4')
        print('Yes')
      #negative output
      else:
        #debugging
        print('fail')
        print('No')