"""
Practical 1: Python Variables, Datatypes and Operators
Task 2: User Input, Type Conversion, and Various Operations

This program demonstrates:
- Taking user input
- Type conversion (string to integer)
- Arithmetic operations (addition, division)
- String operations (membership operator 'in')
- Identity operator (is)
"""

# Take input from user for student name and marks
student_name = input("Enter student's name: ")
marks_str1 = input("Enter marks for subject 1: ")
marks_str2 = input("Enter marks for subject 2: ")
marks_str3 = input("Enter marks for subject 3: ")

# Convert string inputs to integers for mathematical operations
marks1 = int(marks_str1)
marks2 = int(marks_str2)
marks3 = int(marks_str3)

# Calculate total and average marks
total_marks = marks1 + marks2 + marks3
average_marks = total_marks / 3

# Display results with formatted output
print(f"Total Marks: {total_marks}")
print(f"Average Marks: {average_marks:.2f}")

# Check if letter 'A' is present in student name (membership operator)
has_A = "A" in student_name
print(f"Does the name contain 'A'? {has_A}")

# Identity check - comparing if two variables point to same object
m1 = marks1
m2 = marks1
identity_check = m1 is m2
print(f"Identity check: {identity_check}")
