# Write a program that keeps the information about courses. Each course has a name and registered students.
# You will be receiving a course name and a student name until you receive the command "end".
# You should register each user into the corresponding course. If the given course does not exist, add it.
# When you receive the command "end", print the courses with their names and total registered users.
# For each course, print the registered users.
# Input
# •	Until the "end" command is received, you will be receiving input lines in the format:
# "{course_name} : {student_name}"
# •	The product data is always delimited by " : "
# Output
# •	Print the information about each course in the following format:
# "{course_name}: {registered_students}"
# •	Print the information about each student in the following format:
# "-- {student_name}"

courses = {}

command = input()

while not command == 'end':
    current_course = command.split(' : ')
    course_name = current_course[0]
    student_name = current_course[1]
    if course_name not in courses:
        courses[course_name] = []
    courses[course_name].append(student_name)

    command = input()

for course_name in courses.keys():
    students = courses.get(course_name)
    registered_students = len(students)
    print(f"{course_name}: {registered_students}")
    students_in_course = [f"-- {name}" for name in students]
    print(*students_in_course, sep='\n')











