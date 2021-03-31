#https://open.kattis.com/problems/fiftyshades
output = 0
#takes buttons and checks if 'rose' or 'pink' is in the button before incrementing
for i in range (int(input())):
  button = input().lower()
  if ("rose" in button) or ("pink" in button):
    #print(button,"incremented")
    output += 1

#output logic
if output == 0:
  print("I must watch Star Wars with my daughter")
else:
  print(output)