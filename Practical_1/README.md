# Practical 1: Python Variables, Datatypes and Operators

This practical introduces fundamental Python concepts including variables, data types, and operators.

## 📋 Tasks Overview

### Task 1: Basic Variable Declaration and Type Checking
**File:** `task1.py`

#### What You'll Learn:
- How to declare variables in Python
- Different data types (string, integer, float)
- How to print multiple variables
- Using the `type()` function to check data types

#### Code Walkthrough:
```python
name = "Alex"              # String variable
roll_number = 101          # Integer variable
cgpa = 3.8                 # Float variable

print(name, roll_number, cgpa)    # Print all at once
print(type(name))                 # Check type: <class 'str'>
```

#### Expected Output:
```
Alex 101 3.8
<class 'str'>
<class 'int'>
<class 'float'>
```

---

### Task 2: User Input, Type Conversion, and Various Operations
**File:** `task2.py`

#### What You'll Learn:
- Getting user input with `input()`
- Converting strings to integers with `int()`
- Performing arithmetic operations
- Using the membership operator (`in`)
- Using the identity operator (`is`)
- Formatted string output with f-strings

#### Code Walkthrough:
```python
# Get input from user
student_name = input("Enter student's name: ")
marks_str1 = input("Enter marks for subject 1: ")

# Convert to integer for calculations
marks1 = int(marks_str1)

# Calculate total and average
total_marks = marks1 + marks2 + marks3
average_marks = total_marks / 3

# Check if 'A' is in the name
has_A = "A" in student_name
```

#### Key Concepts:
- **Type Conversion:** `input()` always returns a string, so we convert to int
- **Membership Operator:** Checks if one value exists within another
- **Identity Operator:** Checks if two variables reference the same object

#### Expected Interaction:
```
Enter student's name: Ahmad
Enter marks for subject 1: 85
Enter marks for subject 2: 90
Enter marks for subject 3: 88
Total Marks: 263
Average Marks: 87.67
Does the name contain 'A'? True
Identity check: True
```

---

### Task 3: String Operations and Type Demonstrations
**File:** `task3.py`

#### What You'll Learn:
- String indexing (accessing individual characters)
- String slicing (extracting substrings)
- String concatenation (joining strings)
- Operations with mixed data types
- Boolean variables
- Comprehensive type checking

#### Code Walkthrough:

**String Indexing:**
```python
single_quote_string = 'This is a string with single quotes.'
first_char = single_quote_string[0]      # 'T'
last_char = single_quote_string[-1]      # '.'
```

**String Slicing:**
```python
sliced_string = single_quote_string[0:4]  # 'This'
```

**String Concatenation:**
```python
string1 = "Artificial"
string2 = "Intelligence"
joined_string = string1 + " " + string2   # "Artificial Intelligence"
```

**Mixed Type Operations:**
```python
num1 = 20      # Integer
num2 = 5.5     # Float
result = num1 + num2  # 25.5 (result is float)
```

#### Expected Output:
```
This is a string with single quotes.
First character: T
Last character: .
Sliced string: This
Artificial Intelligence
Numeric addition: 25.5
Boolean value: True
Type of 10 is <class 'int'>
Type of 20.5 is <class 'float'>
Type of 'Hello' is <class 'str'>
Type of False is <class 'bool'>
```

---

## 🎯 Learning Objectives

By completing this practical, you will understand:

1. **Variables** - How to store and name data in Python
2. **Data Types** - The different types of data (int, float, str, bool)
3. **Operators** - How to perform operations on data
4. **Type Conversion** - Converting between different data types
5. **User Input** - Getting data from users
6. **String Operations** - Manipulating text data

---

## 🚀 How to Run

1. Open a terminal/command prompt
2. Navigate to the Practical_1 directory:
   ```bash
   cd Practical_1
   ```
3. Run each task:
   ```bash
   python3 task1.py
   python3 task2.py
   python3 task3.py
   ```

---

## 📝 Practice Exercises

Try modifying the code to practice:

1. **Task 1:** Add more variables with different data types
2. **Task 2:** Calculate grades based on average marks
3. **Task 3:** Try different string slicing ranges

---

## 🔑 Key Python Concepts

### Data Types:
- **int** - Whole numbers (e.g., 10, -5, 0)
- **float** - Decimal numbers (e.g., 3.14, -0.5)
- **str** - Text (e.g., "Hello", 'Python')
- **bool** - True or False values

### Operators:
- **Arithmetic:** `+`, `-`, `*`, `/`
- **Membership:** `in`, `not in`
- **Identity:** `is`, `is not`

### Important Functions:
- `print()` - Display output
- `input()` - Get user input
- `type()` - Check data type
- `int()`, `float()`, `str()` - Convert types

---

## ⚠️ Common Mistakes to Avoid

1. **Type Mismatch:** Can't add string and integer directly
   ```python
   # Wrong:
   age = "25"
   new_age = age + 1  # Error!
   
   # Correct:
   age = "25"
   new_age = int(age) + 1  # 26
   ```

2. **Index Out of Range:** Accessing non-existent position
   ```python
   text = "Hello"
   char = text[10]  # Error! Only indices 0-4 exist
   ```

3. **Forgetting Type Conversion:** Input is always string
   ```python
   # Wrong:
   num = input("Enter number: ")
   result = num + 5  # Error!
   
   # Correct:
   num = int(input("Enter number: "))
   result = num + 5
   ```

---

## 📚 Additional Notes

- **Python is dynamically typed:** You don't need to declare variable types
- **Variables names:** Use lowercase with underscores (e.g., `student_name`)
- **Comments:** Use `#` for single-line comments
- **Strings:** Can use single `'` or double `"` quotes

---

**Next:** Move to [Practical 2](../Practical_2/README.md) to learn about Lists!
