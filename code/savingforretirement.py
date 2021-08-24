#https://open.kattis.com/problems/savingforretirement

#needed for math.ceil
import math
#inputs and conversion
b_current, b_future, b_save, a_current, a_save = input().split(' ')
b_current = int(b_current)
b_future = int(b_future)
b_save = int(b_save)
a_current = int(a_current)
a_save = int(a_save)
#amount saved by Bob
b_saved = (b_future-b_current) * b_save
#debugging
print('amount bob has:',b_saved)
#how many years Alice should save
a_should = math.ceil(b_saved/a_save)
#debugging
print('years alice should save for:',a_should)
#how much Alic would've saved
a_saved = (a_should) * a_save
#debugging
print('amount alice has:', a_saved)
#if its equal add 1
if a_saved == b_saved:
  a_should += 1 
#output
print(a_should + a_current)