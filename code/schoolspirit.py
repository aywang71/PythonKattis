#https://open.kattis.com/problems/schoolspirit

def scoreCalc(number, scores):
  score = 0
  for i in range (0,number):
    score += scores[i] * 0.8 ** i
  score = score * 0.2
  return score


n = int(input())
scores = [int(input()) for i in range(n)]
#print(scores)

score = scoreCalc(n,scores)
print(score)

average = 0
newScores = scores.copy()
for i in range (0,n):
  newScores.pop(i)
  #print(newScores)
  average += scoreCalc(n-1,newScores)
  newScores = scores.copy()
  #print('end iteration:', newScores)

print(average/n)