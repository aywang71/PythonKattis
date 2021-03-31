#https://open.kattis.com/problems/coursescheduling

selections = set()
courses = {}

for i in range(int(input())):
    select = input()
    course = select.rsplit(' ',1)[1]
    #print(select)
    if course in courses: 
        pass 
    else:
        courses[course] = 0
    if select not in selections: 
        selections.add(select)
        courses[course] += 1

formats = sorted(courses.items())
#print(formats)

for i in formats:
    print(i[0],i[1])