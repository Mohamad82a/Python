from student_management import add_student, view_students,update_student, create_student, average_calculator, delete_student
from utilities import style, exiting_text, error_text

students = []

def menu():
    while True:
        print('Student Management System')
        print('1. View Students')
        print('2. Add a new Student')
        print('3. Update Student')
        print('4. Delete a Student')
        print("5. Show Student's Grades")
        print("6. Calcute The Student's Average Grade")
        print('7. Exit')

        choice = input('Please Select An Option (1/2/3/4/5/6/7) : ')
        
    
        if choice == '1':
            @style
            def no_info():
                view_students(students)
            no_info()
        
        elif choice == '2':
            student_id = int(input('Please Enter Your Preferred Student ID: '))
            first_name = input("Please Enter The Student's Firstname: ").capitalize()
            last_name = input("Please Enter The Student's Lastname: ").capitalize()
            age = int(input("Please Enter The Student's Age: "))
            courses = input('Enter Courses: ').split(' ')
            grades = {}
            for course in courses:
                cleaned_course = course.strip().capitalize()
                grade = int(input(f'Enter Grade For {cleaned_course}: '))
                grades[cleaned_course] = grade
                
            add_student(students, student_id, first_name, last_name, age, courses, grades)
            
            @style
            def message():
                print(f'*** The Student {first_name} {last_name} With Student ID {student_id} Added Successfulley. ***')
            message()
            
            
            
            
        elif choice == '3':
            update = int(input('Please Enter Preferred Student ID : '))
            for student in students:
                if update == student["Student_ID"]:
                    student_id = int(input('Please Enter Your New Student ID: '))
                    first_name = input("Please Enter The New Firstname: ").capitalize()
                    last_name = input("Please Enter The New Lastname: ").capitalize()
                    age = int(input("Please Enter The New Age: "))
                    courses = input('Enter New Courses: ').split(' ')
                    grades = {}
                    for course in courses:
                        cleaned_course = course.strip().capitalize()
                        grade = int(input(f'Enter New Grade For {cleaned_course}: '))
                        grades[cleaned_course] = grade
                
                    updated_student = create_student(students, student_id, first_name, last_name, age, courses, grades)
                    student.update(updated_student)
                    
                    @style
                    def update_message():
                        print(f'The Student With ID {student_id} Is Successfully Updated')
                    update_message()
                    
                else:
                    print('Student Not Found')

        
        
        elif choice == '4':
            student_id = int(input('Please Enter preferred Student ID To Delete : '))
            @style
            def removed():
                print(f'*** Student {first_name} {last_name} With ID {student_id} Deleted Successfully ***')
            removed()
            
            delete_student(students, student_id)
            
            
            
            
        elif choice == '5':
            which = int(input('Please Enter The Preferred Student ID To View Grades : '))
            for student in students:
                if which == student["Student_ID"]:
                    @style
                    def grade_show():
                        print(f"The Grades Of Student {first_name} {last_name} : {student["Grades"]}")
                    grade_show()
                
                else:
                    print('Student Not Found')
            
            
        
        elif choice == '6':
            which_one = int(input('Please Enter The Preferred Student ID To View Average Grade : '))
            for student in students:
                if which_one == student["Student_ID"]:
                    average_grade = average_calculator(grades)
                    
                    @style
                    def show_grade():
                        print(f"The Average Grade of Student With ID {student_id} is : {average_grade}")
                    show_grade()
                    
                else:
                    print("Student Not Found")
            
        elif choice == '7':
            @style
            def exiting():
                print(f'*** {exiting_text} ***')
            exiting()
            break            

        else:
            @style
            def error():
                print(f'*** {error_text} ***')
            error()

if __name__ == '__main__':
    menu()



