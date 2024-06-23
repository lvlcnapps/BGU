import json

with open('input.txt', 'r') as f:
    ans = json.loads(f.read())
    course = input('Enter course: ')
    print('Students with course', course)
    students = []
    for student, courses in ans.items():
        if course in courses:
            students.append(student)

    if len(students) == 0:
        print('No students found')
    else:
        print(students)
