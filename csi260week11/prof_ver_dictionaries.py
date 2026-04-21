#Working with dictionaries

courses = {'CSI-140':'Intro to C++', 'CSI-160':'Intro to Python', 'CSI-240':'Adv. C++', 'CSI-260':'Adv Python'}
'''
for k in courses.keys():
    print(k)

for v in courses.values():
    print(v)

for k,v in courses.items():
    print(k,v)
'''
grades = {'Exam 1':[89, 87, 91],  'Exam 2':[90, 98, 96], 'Exam 3':[90, 90, 89]}
'''
for k,v in grades.items():
    for i in v:
        print(k,' ',i )
'''
count = 0
for i in range(3):
    for k,v in grades.items():
        print(k,' ',v[count])
    count +=1
