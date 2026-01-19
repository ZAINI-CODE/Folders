students = {}

def add_student():
    student_id = input("Enter student ID: ")
    
    if student_id in students:
        print("Student ID already exists!")
        return
    
    name = input("Enter student name: ")
    try:
        age = int(input("Enter student age: "))
    except ValueError:
        print("Invalid age! Please enter a number.")
        return
    grade = input("Enter student grade: ")
    
    students[student_id] = {
        "name": name,
        "age": age,
        "grade": grade
    }
    print(f"Student {name} added successfully!")

def update_marks():
    student_id = input("Enter student ID to update: ")
    
    if student_id not in students:
        print("Student not found!")
        return
    
    subject = input("Enter subject name: ")
    try:
        marks = float(input("Enter marks: "))
    except ValueError:
        print("Invalid marks! Please enter a number.")
        return
    
    if "marks" not in students[student_id]:
        students[student_id]["marks"] = {}
    
    students[student_id]["marks"][subject] = marks
    print(f"Marks updated for {students[student_id]['name']}")

def delete_student():
    student_id = input("Enter student ID to delete: ")
    
    if student_id not in students:
        print("Student not found!")
        return
    
    name = students[student_id]["name"]
    del students[student_id]
    print(f"Student {name} deleted successfully!")

def print_students():
    if not students:
        print("No students in the system!")
        return
    
    print("\n" + "="*50)
    print("STUDENT RECORDS")
    print("="*50)
    
    for student_id, details in students.items():
        print(f"\nStudent ID: {student_id}")
        print(f"Name: {details['name']}")
        print(f"Age: {details['age']}")
        print(f"Grade: {details['grade']}")
        
        if "marks" in details:
            print("Marks:")
            for subject, marks in details["marks"].items():
                print(f"  {subject}: {marks}")
    
    print("="*50)

def main():
    while True:
        print("\n" + "="*50)
        print("STUDENT MANAGEMENT SYSTEM")
        print("="*50)
        print("1. Add Student")
        print("2. Update Marks")
        print("3. Delete Student")
        print("4. Display All Students")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            add_student()
        elif choice == '2':
            update_marks()
        elif choice == '3':
            delete_student()
        elif choice == '4':
            print_students()
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

main()
