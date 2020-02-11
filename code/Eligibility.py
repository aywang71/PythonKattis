#https://open.kattis.com/problems/eligibility

#iteration input
n = int(input())
#runs iterations
for i in range (0,n):
  #more inptus
  name, school, birth, courses = input().split(" ")
  #pairs and splits
  courses = int(courses)/5
  school = school.split('/')
  birth = birth.split('/')
  #output format
  if int(school[0])>=2010:
    print(name, 'eligible')
  elif int(birth[0])>=1991:
    print(name,' eligible')
  elif courses <= 8:
    print(name,'coach petitions')
  else:
    print(name, 'ineligible')

