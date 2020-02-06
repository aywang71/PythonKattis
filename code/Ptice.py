#https://open.kattis.com/problems/ptice

#lists and variables for correct and sequence
A = ['A','B','C']
Acorrect = 0
B = ['B','A','B','C']
Bcorrect = 0
G = ['C','C','A','A','B','B']
Gcorrect = 0
#inputs
number = int(input())
answers = list(input())
#finds amount of correct inputs
for i in range (0,len(answers)):
  if answers[i] == A[i%len(A)]:
    Acorrect += 1
  if answers[i] == B[i%len(B)]:
    Bcorrect += 1
  if answers[i] == G[i%len(G)]:
    Gcorrect += 1
#files in more lists
most_correct = []
correct = [Acorrect,Bcorrect,Gcorrect]
correctest = 0
#debugging
print(Acorrect)
print(Bcorrect)
print(Gcorrect)
#finds largest corrects
for i in range (0,len(correct)):
  if correctest < correct[i]:
    correctest = correct[i]
#finds names
if Acorrect == correctest:
  most_correct.append("Adrian")
if Bcorrect == correctest:
  most_correct.append("Bruno")
if Gcorrect == correctest:
  most_correct.append("Goran ")
#output format
print(correctest)
for i in range (0,len(most_correct)):
  print(most_correct[i])
