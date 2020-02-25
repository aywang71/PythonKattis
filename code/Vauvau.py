#https://open.kattis.com/problems/vauvau

#finds the amount of dogs
def find_dog (remainder1,remainder2,dog1, dog2):
  #count for dogs that attack
  count = 0
  if remainder1 > dog1:
    #debugging
    print(remainder1,'>',dog1)
    count += 1 
  elif remainder1 == 0:
    #debugging
    print('is 0')
    count += 1
  if remainder2 > dog2:
    #debugging
    print(remainder2,'>',dog2)
    count += 1
  elif remainder2 == 0:
    #debugging
    print('is 0')
    count += 1
  #return format
  if count == 0:
    return 'both'
  elif count == 1:
    return 'one'
  elif count == 2:
    return 'none'

#input and formatting
dog1a, dog2a, dog1b, dog2b = input().split(' ')
p,m,g = input().split(' ')
dog1a = int(dog1a)
dog1b = int(dog1b)
dog2a = int(dog2a)
dog2b = int(dog2b)
p = int(p)
m = int(m)
g = int(g)
#finding remainders
p1 = p%(dog1a+dog2a)
p2 = p%(dog1b+dog2b)
m1 = m%(dog1a+dog2a)
m2 = m%(dog1b+dog2b)
g1 = g%(dog1a+dog2a)
g2 = g%(dog1b+dog2b)
#output format
print(find_dog(p1,p2,dog1a,dog1b))
print(find_dog(m1,m2,dog1a,dog1b))
print(find_dog(g1,g2,dog1a,dog1b))