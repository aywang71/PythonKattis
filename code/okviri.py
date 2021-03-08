#https://open.kattis.com/problems/okviri

#input
string = list(input())
#debugging
print(string)
# sets up lists, because the edges of frames must intersect
row51 = ['..#..']
row42 = ['.#.#.']
row3 = [''.join(['#','.',string[0],'.','#'])]
#goes through to set up lists
for i in range(1,len(string)):
  row51.append('.#..')
  row42.append('#.#.')
  row3.append(''.join(['.',string[i],'.','#']))
#goes to every third letter and sets it to a '*' format
for i in range(2,len(string),3):
  #debugging
  print(i)
  row51[i] = '.*..'
  row42[i] = '*.*.'
  row3[i-1] = ''.join(['.',string[i-1],'.','*'])
  row3[i] = ''.join(['.',string[i],'.','*'])
#debugging
print(row51)
print(row42)
print(row3)
#output
print(''.join(row51))
print(''.join(row42))
print(''.join(row3))
print(''.join(row42))
print(''.join(row51))


  