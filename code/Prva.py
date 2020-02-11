#https://open.kattis.com/problems/prva

#inptu format
rows, columns = input().split(' ')
rows = int(rows)
columns = int(columns)
crossword = []
#appends rows to virtual grid
for i in range (0,rows):
  row = list(input())
  crossword.append(row)
possible_words = []
#possible_words includes all rows 
for i in range (0,rows):
  possible_words.append(''.join(crossword[i]))
#gets possible_words for all columns
for i in range (0,columns):
  temp_list = []
  for x in range (0,rows):
     temp_list.append(crossword[x][i])
  possible_words.append(''.join(temp_list))
#debugging
print(possible_words)
final_selection = []
#goes through to find words without "#"
for i in range (0,len(possible_words)):
  if "#" in possible_words[i]:
    #starts a coutner variable to measure where we are in the possible_words[i]
    x = 0
    while x < len(possible_words[i])-1:
      #as long as we have two or more consecutive characters
      if (possible_words[i][x] != "#") and (possible_words[i][x+1] != "#"):
        temp_list = []
        #go through until they are no longer conscutive
        while (possible_words[i][x] != "#") :
          temp_list.append(possible_words[i][x])
          #debugging
          print(possible_words[i][x])
          #breaks if length too much
          if x < len(possible_words[i])-1:
            x+= 1
          else:
            break
        #appends consecutive characters to final_selection
        final_selection.append(''.join(temp_list))
      x += 1
  #if length of possible_words[i] is too little
  elif len(possible_words[i])<2:
    continue
  #if everything is fine
  else:
    final_selection.append(possible_words[i])
#debugging
print(final_selection)
#output format
print(min(final_selection))
