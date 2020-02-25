#https://open.kattis.com/problems/exam

#input
correct = int(input())
my_ans = list(input())
fr_ans = list(input())
same = 0
#gets number of same things
for i in range (0,len(my_ans)):
  if my_ans[i] == fr_ans[i]:
    same += 1
#calculates, anything that is the same will be correct (var1)
if same > correct:
  var1 = correct
  correct = 0
else:
  var1 = same
  correct = correct-same
#takes the remainder of things correct, and subtracts it from the different things
var2 = len(my_ans)-same-correct
#output
print(var1+var2)