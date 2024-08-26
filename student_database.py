# Write your solution here
#In this series of exercises you will create a simple student database. Before diving in, please spend a moment reading through the instructions and thinking about what sort of data structures are necessary for organising the data stored by your program.

#Part 1
#First write a function named add_student, which adds a new student to the database.
def add_student(students, name):
    if name not in students:
        students[name] = []
    
#Part 1
#Also write a preliminary version of the function print_student, which prints out the information of a single student.
def print_student(students, name):
    print(f"{name}:", end="")
    if name in students:
        courses_taken = len(students[name])
        if courses_taken <= 0:
            print("\n no completed courses")
        else:
            total_grade = 0
            print(f"\n {len(students[name])} completed courses:")
            for course, grade in students[name]:
                print(f"  {course} {grade}")
                total_grade += grade
            print(f" average grade {total_grade/courses_taken}")
    else:
        print(" no such person in the database")

#Part 2
#Please write a function named add_course, which adds a completed course to the information of a specific student in the database. The course data is a tuple consisting of the name of the course and the grade:
#Part 3
#Courses with grade 0 should be ignored when adding course information. Additionally, if the course is already in the database in that specific student's information, the grade recorded in the database should never be lowered if the course is repeated.
def add_course(students, name, course):
    if name in students:
        if course[1] != 0:
            for courses in students[name]:
                if courses[0] == course[0]:
                    old_grade = courses[1]
                    students[name].remove(courses)
                    students[name].append((course[0], max([old_grade, course[1]])))
                    return None
            students[name].append(course)

#Part 4
#Please write a function named summary, which prints out a summary based on all the information stored in the database.
def summary(students):
    total_students = 0
    most_courses = "",0
    best_average = "",0
    for name, courses in students.items():
        total_grades = 0
        courses_taken = len(courses)
        for course in courses:
            total_grades += course[1]
        if most_courses[1] < courses_taken:
            most_courses = name, courses_taken
        if best_average[1] < (total_grades/courses_taken):
            best_average = (name, (total_grades/courses_taken))
        total_students += 1
    print(f"students {total_students}")
    print(f"most courses completed {most_courses[1]} {most_courses[0]}")
    print(f"best average grade {best_average[1]} {best_average[0]}")
        
        
if __name__ == "__main__":
#Part 1 - adding Student
    # students = {}
    # add_student(students, "Peter")
    # add_student(students, "Eliza")
    # print_student(students, "Peter")
    # print_student(students, "Eliza")
    # print_student(students, "Jack")

#Part 2 - adding completed courses
    # students = {}
    # add_student(students, "Peter")
    # add_course(students, "Peter", ("Introduction to Programming", 3))
    # add_course(students, "Peter", ("Advanced Course in Programming", 2))
    # print_student(students, "Peter")

#Part 3 - Repeating courses
    # students = {}
    # add_student(students, "Peter")
    # add_course(students, "Peter", ("Introduction to Programming", 3))
    # add_course(students, "Peter", ("Advanced Course in Programming", 2))
    # add_course(students, "Peter", ("Data Structures and Algorithms", 0))
    # add_course(students, "Peter", ("Introduction to Programming", 2))
    # print_student(students, "Peter")

#Part 4 - Summary of datavase
    students = {}
    add_student(students, "Peter")
    add_course(students, "Peter", ("Introduction to Programming", 3))
    add_course(students, "Peter", ("Advanced Course in Programming", 2))
    add_course(students, "Peter", ("Data Structures and Algorithms", 0))
    add_course(students, "Peter", ("Introduction to Programming", 2))
    print_student(students, "Peter")
