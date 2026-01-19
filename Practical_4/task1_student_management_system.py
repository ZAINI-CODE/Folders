"""
Practical 4: Functions and Modules in Python
Task 1: Student Management System with Functions

This program demonstrates:
- Function definition and calling
- Global dictionary for data storage
- Input validation
- CRUD operations (Create, Read, Update, Delete)
- Menu-driven program structure
- While loop for continuous operation
"""

# Global dictionary to store student records
students = {}

def add_student():
    """Add a new student to the system"""
    student_id = input("Enter student ID: ")
    
    # Check if student already exists
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
    
    # Add student to dictionary
    students[student_id] = {
        "name": name,
        "age": age,
        "grade": grade
    }
    print(f"Student {name} added successfully!")

def update_marks():
    """Update marks for an existing student"""
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
    
    # Add or update marks for the subject
    if "marks" not in students[student_id]:
        students[student_id]["marks"] = {}
    
    students[student_id]["marks"][subject] = marks
    print(f"Marks updated for {students[student_id]['name']}")

def delete_student():
    """Delete a student from the system"""
    student_id = input("Enter student ID to delete: ")
    
    if student_id not in students:
        print("Student not found!")
        return
    
    name = students[student_id]["name"]
    del students[student_id]
    print(f"Student {name} deleted successfully!")

def print_students():
    """Display all students in the system"""
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
    """Main function to run the student management system"""
    while True:
        # Display menu
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

# Run the program
main()
