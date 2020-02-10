#https://open.kattis.com/problems/acm

#array for storage
problems_done = []
problems_attempted = []
time = 0
while True:
  try:
    #inputs
    time_amount, problem, status = input().split(' ')
    time_amount = int(time_amount)
  except:
    break
  #if correct, add to total
  if status == "right":
    problems_done.append(problem)
    time_problem = time_amount + (problems_attempted.count(problem)*20)
    #debugging
    print("time:",time_problem)
    time += time_problem
    #debugging
    print("Total:",time)
  #time penalties for wrong
  if status == "wrong" :
    problems_attempted.append(problem)
#debugging
print(len(problems_done),time)
  

