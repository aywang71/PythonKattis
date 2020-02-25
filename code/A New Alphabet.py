#https://open.kattis.com/problems/anewalphabet

#dictionary conversion key
conversion = {
  'a':'@',
  'b':'8',
  'c':'(',
  'd':'|)',
  'e':'3',
  'f':'#',
  'g':'6',
  'h':'[-]',
  'i':'|',
  'j':'_|',
  'k':'|<',
  'l':'1',
  'm':'[]\/[]',
  'n':'[]\[]',
  'o':'0',
  'p':'|D',
  'q':'(,)',
  'r':'|Z',
  's':'$',
  't':"']['",
  'u':'|_|',
  'v':'\/',
  'w':'\/\/',
  'x':'}{',
  'y':'`/',
  'z':'2',
  ' ':' ',
  ',':',',
  "'":"'",
  '.':'.',
  '?':'?',
  '!':'!',
}
#input
string =  list(input())
#converts
for i in range (0,len(string)):
  x = string[i]
  #checks if in conversion first
  if x.lower() in conversion:
    string[i] = conversion[x.lower()]
#output
print(''.join(string))