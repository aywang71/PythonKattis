maxScore = 0
num = 0;

for j in range(5):
  x = input().split(' ')
  for i in range(len(x)):
    x[i] = int(x[i])
  #print(x, sum(x))
  if sum(x) > maxScore:
    maxScore = sum(x)
    #print("j:", j+1)
    num = j + 1
print(num, maxScore)