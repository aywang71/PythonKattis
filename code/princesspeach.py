#https://open.kattis.com/problems/princesspeach

#inputs for obstacles and encounters 
obstacles, encounters = input().split(' ')
#obstacles to integer
obstacles = int(obstacles)
#storages for list, encounters, and uniqes
list_obstacles = []
obstacles_encounter = []
unique_obstacles = []
#makes list for obstacles
for i in range (0,obstacles):
  list_obstacles.append(i)
#encounters to integer
encounters = int(encounters)
#gets encounter number of obstacle_numbers to append to encounter list
for i in range (0,encounters):
  obstacle_number = int(input())
  obstacles_encounter.append(obstacle_number)
  #assembles unique list
  if obstacle_number in unique_obstacles:
    continue
  else:
    unique_obstacles.append(obstacle_number)
#debugging
print(list_obstacles)
print(obstacles_encounter)
print(unique_obstacles)
#Removing encountered obstacles
for i in range (0,len(obstacles_encounter)):
  if obstacles_encounter[i] in  list_obstacles:
    list_obstacles.remove(obstacles_encounter[i])
  else:
    continue
#debugging
print(list_obstacles)
#output format
for i in range (0,len(list_obstacles)):
  print(list_obstacles[i])
print("Mario got %i of the dangerous obstacles."%(len(unique_obstacles)))
