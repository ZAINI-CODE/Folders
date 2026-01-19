# Practical 4: Functions and Modules in Python

This practical introduces functions in Python and demonstrates how to organize code into reusable, modular components.

## 📋 Tasks Overview

### Task 1: Student Management System with Functions
**File:** `task1_student_management_system.py`

#### What You'll Learn:
- Defining and calling functions
- Function parameters and return values
- Using docstrings for documentation
- Global variables for data persistence
- Building menu-driven applications
- CRUD operations (Create, Read, Update, Delete)
- Input validation

#### Program Structure:
```python
# Global data storage
students = {}

# Function definitions
def add_student():
    # Implementation

def update_marks():
    # Implementation

def delete_student():
    # Implementation

def print_students():
    # Implementation

def main():
    # Main program loop

# Program entry point
main()
```

#### Code Walkthrough:

**Function Definition with Docstring:**
```python
def add_student():
    """Add a new student to the system"""
    # Function implementation
```

**Global Data Storage:**
```python
# Dictionary to store all student records
students = {
    "S001": {
        "name": "John",
        "age": 20,
        "grade": "A",
        "marks": {"Math": 95, "Physics": 88}
    }
}
```

**Add Student Function:**
```python
def add_student():
    """Add a new student to the system"""
    student_id = input("Enter student ID: ")
    
    # Check if student already exists
    if student_id in students:
        print("Student ID already exists!")
        return
    
    name = input("Enter student name: ")
    age = int(input("Enter student age: "))
    grade = input("Enter student grade: ")
    
    # Add to dictionary
    students[student_id] = {
        "name": name,
        "age": age,
        "grade": grade
    }
    print(f"Student {name} added successfully!")
```

**Update Marks Function:**
```python
def update_marks():
    """Update marks for an existing student"""
    student_id = input("Enter student ID to update: ")
    
    if student_id not in students:
        print("Student not found!")
        return
    
    subject = input("Enter subject name: ")
    marks = float(input("Enter marks: "))
    
    # Initialize marks dictionary if it doesn't exist
    if "marks" not in students[student_id]:
        students[student_id]["marks"] = {}
    
    students[student_id]["marks"][subject] = marks
    print(f"Marks updated for {students[student_id]['name']}")
```

**Delete Student Function:**
```python
def delete_student():
    """Delete a student from the system"""
    student_id = input("Enter student ID to delete: ")
    
    if student_id not in students:
        print("Student not found!")
        return
    
    name = students[student_id]["name"]
    del students[student_id]
    print(f"Student {name} deleted successfully!")
```

**Display Students Function:**
```python
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
```

**Main Function with Menu:**
```python
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
```

#### Expected Interaction:
```
==================================================
STUDENT MANAGEMENT SYSTEM
==================================================
1. Add Student
2. Update Marks
3. Delete Student
4. Display All Students
5. Exit
Enter your choice: 1
Enter student ID: S001
Enter student name: John Doe
Enter student age: 20
Enter student grade: A
Student John Doe added successfully!

==================================================
STUDENT MANAGEMENT SYSTEM
==================================================
1. Add Student
2. Update Marks
3. Delete Student
4. Display All Students
5. Exit
Enter your choice: 2
Enter student ID to update: S001
Enter subject name: Mathematics
Enter marks: 95
Marks updated for John Doe

==================================================
STUDENT MANAGEMENT SYSTEM
==================================================
1. Add Student
2. Update Marks
3. Delete Student
4. Display All Students
5. Exit
Enter your choice: 4

==================================================
STUDENT RECORDS
==================================================

Student ID: S001
Name: John Doe
Age: 20
Grade: A
Marks:
  Mathematics: 95.0
==================================================
```

---

## 🎯 Learning Objectives

By completing this practical, you will understand:

1. **Function Definition** - Creating reusable code blocks
2. **Function Parameters** - Passing data to functions
3. **Return Values** - Getting data from functions
4. **Docstrings** - Documenting functions
5. **Global Variables** - Sharing data across functions
6. **Menu-Driven Programs** - User interaction patterns
7. **CRUD Operations** - Create, Read, Update, Delete
8. **Input Validation** - Checking user input
9. **Program Organization** - Structuring larger programs

---

## 🚀 How to Run

1. Open a terminal/command prompt
2. Navigate to the Practical_4 directory:
   ```bash
   cd Practical_4
   ```
3. Run the program:
   ```bash
   python3 task1_student_management_system.py
   ```
4. Follow the menu prompts to interact with the system

---

## 📝 Practice Exercises

Try these enhancements:

1. **Add More Features:**
   - Calculate average marks for each student
   - Find student with highest marks
   - Sort students by name or grade
   - Search for students by name

2. **Add Validation:**
   - Ensure age is positive
   - Validate grade is A-F
   - Check marks are 0-100
   - Prevent empty names

3. **Add More Functions:**
   - `search_student(name)` - Find by name
   - `calculate_average(student_id)` - Calculate avg marks
   - `get_top_student()` - Find highest scorer
   - `export_to_file()` - Save data to file

4. **Improve UI:**
   - Add colors to output
   - Clear screen between operations
   - Add confirmation for delete
   - Show statistics dashboard

---

## 🔑 Key Function Concepts

### Function Definition:
```python
def function_name(parameters):
    """Docstring describing the function"""
    # Function body
    return value  # Optional
```

### Types of Functions:

**1. Function with No Parameters and No Return:**
```python
def greet():
    print("Hello!")

greet()  # Call the function
```

**2. Function with Parameters:**
```python
def greet_person(name):
    print(f"Hello, {name}!")

greet_person("Alice")
```

**3. Function with Return Value:**
```python
def add(a, b):
    return a + b

result = add(5, 3)  # result = 8
```

**4. Function with Default Parameters:**
```python
def greet(name="Guest"):
    print(f"Hello, {name}!")

greet()          # Uses default: "Hello, Guest!"
greet("Alice")   # "Hello, Alice!"
```

**5. Function with Multiple Return Values:**
```python
def get_min_max(numbers):
    return min(numbers), max(numbers)

minimum, maximum = get_min_max([1, 5, 3, 9, 2])
```

---

## ⚠️ Common Mistakes to Avoid

1. **Forgetting to Call the Function:**
   ```python
   def my_function():
       print("Hello")
   
   # Wrong: Just defining doesn't run it
   my_function  # Missing parentheses!
   
   # Correct:
   my_function()
   ```

2. **Global Variable Modification:**
   ```python
   count = 0
   
   def increment():
       global count  # Need global keyword to modify
       count += 1
   ```

3. **Not Returning a Value:**
   ```python
   # Wrong:
   def add(a, b):
       result = a + b
       # Forgot to return!
   
   # Correct:
   def add(a, b):
       return a + b
   ```

4. **Modifying Mutable Default Parameters:**
   ```python
   # Dangerous:
   def append_to(item, list=[]):
       list.append(item)
       return list
   
   # Safe:
   def append_to(item, list=None):
       if list is None:
           list = []
       list.append(item)
       return list
   ```

---

## 📚 Function Best Practices

### 1. Single Responsibility:
Each function should do one thing well.
```python
# Good: Each function has one job
def calculate_total(marks):
    return sum(marks)

def calculate_average(marks):
    return calculate_total(marks) / len(marks)
```

### 2. Descriptive Names:
Use verb-noun combinations.
```python
# Good function names:
def get_student_data()
def calculate_average_marks()
def validate_input()
def print_report()
```

### 3. Use Docstrings:
```python
def calculate_grade(marks):
    """
    Calculate letter grade based on marks.
    
    Args:
        marks (float): Student's marks (0-100)
    
    Returns:
        str: Letter grade (A, B, C, D, or F)
    """
    if marks >= 90:
        return 'A'
    # ... rest of implementation
```

### 4. Keep Functions Short:
Aim for functions that fit on one screen.

### 5. Limit Parameters:
Too many parameters make functions hard to use.
```python
# Instead of many parameters:
def create_student(name, age, grade, marks, address, phone):
    pass

# Use a dictionary:
def create_student(student_data):
    pass
```

---

## 💡 Advanced Function Concepts

### Lambda Functions:
Short anonymous functions for simple operations.
```python
# Regular function
def square(x):
    return x ** 2

# Lambda equivalent
square = lambda x: x ** 2

# Common use with sorted()
students.sort(key=lambda s: s['name'])
```

### *args and **kwargs:
Variable number of arguments.
```python
def sum_all(*args):
    return sum(args)

sum_all(1, 2, 3, 4, 5)  # 15

def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="John", age=30, city="NYC")
```

---

## 🔗 Function Scope

### Local Scope:
Variables defined inside functions are local.
```python
def my_function():
    local_var = 10  # Only accessible inside function
    print(local_var)
```

### Global Scope:
Variables defined outside all functions.
```python
global_var = 20

def my_function():
    print(global_var)  # Can read global variable
```

### Modifying Global Variables:
```python
count = 0

def increment():
    global count
    count += 1  # Modify global variable
```

---

## 📖 Complete Example: Grade Calculator

```python
def get_letter_grade(marks):
    """Convert numeric marks to letter grade"""
    if marks >= 90:
        return 'A'
    elif marks >= 80:
        return 'B'
    elif marks >= 70:
        return 'C'
    elif marks >= 60:
        return 'D'
    else:
        return 'F'

def calculate_average(marks_dict):
    """Calculate average from marks dictionary"""
    if not marks_dict:
        return 0
    return sum(marks_dict.values()) / len(marks_dict)

def generate_report(student):
    """Generate student report"""
    print(f"\nReport for {student['name']}")
    print("=" * 40)
    
    for subject, marks in student['marks'].items():
        grade = get_letter_grade(marks)
        print(f"{subject}: {marks} ({grade})")
    
    avg = calculate_average(student['marks'])
    avg_grade = get_letter_grade(avg)
    print(f"\nAverage: {avg:.2f} ({avg_grade})")
```

---

**Congratulations!** You've completed the fundamentals of Python programming. These four practicals have covered:
- Variables and operators
- Lists and data structures
- Dictionaries
- Functions and program organization

Continue practicing and building projects to strengthen your skills!
