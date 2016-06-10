__author__ = 'Dr.S.Gowrishankar'

studentname = {}
ave = 0.0

num = int(raw_input('Enter the number of students'))

for i in range(0,num):
    name = raw_input('Enter the name of the student')
    roll_number = raw_input('Enter the roll number')
    marks = raw_input('Enter the marks for each of the student')

    studentname[name] = (roll_number, marks)

student_search = raw_input('Enter the name of the student you want to search')

if student_search not in studentname:
    print 'the student you are searching is not present in the class'
else:
    print 'the student you are searching is present in the class'

stu_marks = []
for name in studentname:
    stu_marks.append(int(studentname[name][1]))

ave = float(sum(stu_marks)/len(stu_marks))

print 'The average marks of the class is {0}'.format(ave)

