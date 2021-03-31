#https://open.kattis.com/problems/finalexam2

answers = []
count = 0

for i in range(int(input())): answers.append(input())

#print(answers)

for i in range(len(answers)-1):
  if answers[i] == answers[i+1]: count += 1

print(count)