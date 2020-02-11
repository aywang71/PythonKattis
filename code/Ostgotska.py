#https://open.kattis.com/problems/ostgotska

#input
sentence = input().split(' ')
#debugging
print(sentence)
#counts for EA
count = 0
#run coutner
for i in sentence:
  if 'ae' in i:
    count += 1
#debugging
print(count)
#output format
if (count/len(sentence)) >= 0.4:
  print('dae ae ju traeligt va')
else:
  print('haer talar vi rikssvenska')