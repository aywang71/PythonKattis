#https://open.kattis.com/problems/sok

#inputs
input1,input2,input3 = input().split(' ')
input1 = int(input1)
input2 = int(input2)
input3 = int(input3)
#files into list
used = [input1,input2,input3]
#more inputs
ratio1, ratio2, ratio3 = input().split(' ')
ratio1 = int(ratio1)
ratio2 = int(ratio2)
ratio3 = int(ratio3)
#another list
ratios = [ratio1,ratio2,ratio3]
#amount used per ingredient 
combos = [input1/ratio1,input2/ratio2,input3/ratio3]
#checks if the ingredient amount is the same
if (input1 == input2) and (input2 == input3):
  ratio = input1/max(ratios)
else:
  #otherwise simply make the ratio the least amount made
  ratio = used[combos.index(min(combos))]/ratios[combos.index(min(combos))]
#debugging
print(ratio)
#how much is used
input1_correct = input1-(ratio1*ratio)
input2_correct = input2-(ratio2*ratio)
input3_correct = input3-(ratio3*ratio)
#format and output
juice = [str(input1_correct),str(input2_correct),str(input3_correct)]
print(' '.join(juice))