# Python Programming Practicals

This repository contains Python programming practicals covering fundamental to advanced concepts. Each practical is organized in its own directory with properly commented code and documentation.

## 📚 Table of Contents

1. [Practical 1: Python Variables, Datatypes and Operators](#practical-1)
2. [Practical 2: Implementing Data Structures List and Set](#practical-2)
3. [Practical 3: Dictionaries and Tuples in Python](#practical-3)
4. [Practical 4: Functions and Modules in Python](#practical-4)
5. [Practical 5: File Handling in Python](#practical-5)
6. [Practical 6: Object-Oriented Programming in Python](#practical-6)
7. [Practical 7: Exception Handling and Modules](#practical-7)
8. [Practical 8: Advanced Python Concepts](#practical-8)
9. [How to Run](#how-to-run)
10. [Requirements](#requirements)

---

## Practical 1: Python Variables, Datatypes and Operators

**Location:** `Practical_1/`

This practical covers the basics of Python programming including variables, data types, and operators.

### Tasks:

#### Task 1: Basic Variable Declaration and Type Checking
**File:** `task1.py`

- Variable declaration with different data types (string, integer, float)
- Printing multiple variables
- Type checking using `type()` function

**Concepts Covered:**
- String variables
- Integer variables
- Float variables
- `type()` function

#### Task 2: User Input, Type Conversion, and Various Operations
**File:** `task2.py`

- Taking user input
- Type conversion (string to integer)
- Arithmetic operations (addition, division)
- String membership operator (`in`)
- Identity operator (`is`)

**Concepts Covered:**
- `input()` function
- Type casting with `int()`
- Arithmetic calculations
- Formatted output with f-strings
- Membership and identity operators

#### Task 3: String Operations and Type Demonstrations
**File:** `task3.py`

- String indexing and slicing
- String concatenation
- Mixed data type operations
- Boolean variables
- Comprehensive type checking

**Concepts Covered:**
- String indexing (`[0]`, `[-1]`)
- String slicing (`[0:4]`)
- String concatenation
- Float and integer operations
- Boolean data type

---

## Practical 2: Implementing Data Structures List and Set

**Location:** `Practical_2/`

This practical focuses on Python's list data structure and various list operations.

### Tasks:

#### Grocery List Task
**File:** `grocery_list_task.py`

- List creation and initialization
- Adding items using `extend()` and `insert()`
- Removing items using `remove()`
- Finding item position using `index()`
- List slicing

**Concepts Covered:**
- List creation
- `extend()` method
- `insert()` method
- `remove()` method
- `index()` method
- List slicing

#### Task 1: Hospital Patient Management System
**File:** `task1_hospital_patient_management.py`

A comprehensive program demonstrating nested lists (2D lists) and various list operations:

- Creating and managing patient records
- Adding patients (`append()`, `insert()`, `extend()`)
- Removing patients (search and remove, `pop()`)
- List comprehension for data extraction
- Sorting and reversing lists
- Creating independent copies with `copy()`
- Updating nested list elements

**Concepts Covered:**
- Nested lists (2D lists)
- `append()` method
- `insert()` method
- `extend()` method
- `remove()` method
- `pop()` and `pop(index)` methods
- List comprehension
- `sort()` and `reverse()` methods
- `copy()` method
- Positive and negative indexing
- Element updating

---

## Practical 3: Dictionaries and Tuples in Python

**Location:** `Practical_3/`

This practical explores Python dictionaries with nested structures.

### Tasks:

#### Task 1: AI Patient Monitoring System
**File:** `task1_ai_patient_monitoring.py`

A sophisticated program using nested dictionaries to manage patient data:

- Creating nested dictionaries
- Accessing and manipulating dictionary data
- Using `keys()`, `values()`, and `items()` methods
- List comprehension with dictionaries
- Dictionary comprehension
- Statistical calculations from dictionary data
- Conditional filtering

**Concepts Covered:**
- Nested dictionaries
- `keys()`, `values()`, `items()` methods
- Dictionary comprehension
- List comprehension with dictionaries
- Adding and updating dictionary entries
- `pop()` method for dictionaries
- Membership testing with `in`
- Statistical operations

---

## Practical 4: Functions and Modules in Python

**Location:** `Practical_4/`

This practical introduces functions and program organization.

### Tasks:

#### Task 1: Student Management System with Functions
**File:** `task1_student_management_system.py`

A complete menu-driven application demonstrating:

- Function definition and calling
- Global data storage
- CRUD operations (Create, Read, Update, Delete)
- Input validation
- Menu-driven interface

**Concepts Covered:**
- Function definition (`def`)
- Function parameters and return values
- Global variables
- Docstrings
- While loops
- Conditional statements
- Menu-driven programming

---

## Practical 5: File Handling in Python

**Location:** `Practical_5/`

This practical covers file operations in Python.

### Topics:
- Opening and closing files
- Reading from files
- Writing to files
- File modes (read, write, append)
- Working with CSV files
- Exception handling for file operations

**Status:** Documentation available. Code examples coming soon.

---

## Practical 6: Object-Oriented Programming in Python

**Location:** `Practical_6/`

This practical introduces OOP concepts in Python.

### Topics:
- Classes and objects
- Constructors (`__init__`)
- Instance variables and methods
- Class variables
- Inheritance
- Encapsulation
- Polymorphism

**Status:** Documentation available. Code examples coming soon.

---

## Practical 7: Exception Handling and Modules

**Location:** `Practical_7/`

This practical covers error handling and modules.

### Topics:
- Try-except blocks
- Handling multiple exceptions
- Finally clause
- Raising exceptions
- Creating custom exceptions
- Importing modules
- Creating custom modules

**Status:** Documentation available. Code examples coming soon.

---

## Practical 8: Advanced Python Concepts

**Location:** `Practical_8/`

This practical covers advanced Python programming.

### Topics:
- Advanced list comprehensions
- Generator expressions
- Decorators
- Lambda functions
- Map, filter, and reduce
- Regular expressions
- Working with JSON

**Status:** Documentation available. Code examples coming soon.

---

## How to Run

### Running Individual Files

1. Navigate to the practical directory:
   ```bash
   cd Practical_1
   ```

2. Run the Python file:
   ```bash
   python3 task1.py
   ```

### Running All Files in a Practical

You can run each task file individually to see the output:

```bash
# Practical 1
python3 Practical_1/task1.py
python3 Practical_1/task2.py
python3 Practical_1/task3.py

# Practical 2
python3 Practical_2/grocery_list_task.py
python3 Practical_2/task1_hospital_patient_management.py

# Practical 3
python3 Practical_3/task1_ai_patient_monitoring.py

# Practical 4
python3 Practical_4/task1_student_management_system.py
```

---

## Requirements

- **Python Version:** Python 3.6 or higher
- **Operating System:** Windows, macOS, or Linux
- **No External Libraries:** All practicals use Python standard library only

### Checking Python Version

```bash
python3 --version
```

---

## Learning Path

### For Beginners:
1. Start with **Practical 1** to understand basic Python syntax
2. Move to **Practical 2** to learn about lists
3. Progress to **Practical 3** for dictionaries
4. Complete **Practical 4** to understand functions
5. Continue with **Practicals 5-8** for advanced topics

### Key Concepts by Practical:

| Practical | Key Concepts | Status |
|-----------|-------------|--------|
| Practical 1 | Variables, Data Types, Operators, Type Conversion | ✅ Complete |
| Practical 2 | Lists, List Methods, Nested Lists, List Comprehension | ✅ Complete |
| Practical 3 | Dictionaries, Nested Dictionaries, Dictionary Methods | ✅ Complete |
| Practical 4 | Functions, Parameters, Return Values, Program Organization | ✅ Complete |
| Practical 5 | File Handling, Reading/Writing Files, CSV | 📝 Coming Soon |
| Practical 6 | OOP, Classes, Objects, Inheritance | 📝 Coming Soon |
| Practical 7 | Exception Handling, Modules, Custom Exceptions | 📝 Coming Soon |
| Practical 8 | Advanced Concepts, Decorators, Generators, Regex | 📝 Coming Soon |

---

## Code Structure

Each Python file follows this structure:

1. **Module Docstring** - Describes the file's purpose and concepts
2. **Code Sections** - Organized with comments explaining each part
3. **Inline Comments** - Explain specific lines or operations

### Example:
```python
"""
Module docstring explaining the file
"""

# Section comment
variable = value  # Inline comment explaining this line

# Another section
function_call()  # What this does
```

---

## Tips for Learning

1. **Read the Comments:** Each file has detailed comments explaining the code
2. **Modify and Experiment:** Try changing values and see what happens
3. **Run Frequently:** Execute code after each change to see results
4. **Understand Before Moving On:** Make sure you understand one concept before moving to the next
5. **Practice:** Try creating similar programs with different data

---

## Common Python Commands Used

| Command | Purpose |
|---------|---------|
| `print()` | Display output |
| `input()` | Get user input |
| `type()` | Check data type |
| `int()`, `float()`, `str()` | Type conversion |
| `len()` | Get length |
| `.append()` | Add to end of list |
| `.insert()` | Add at specific position |
| `.remove()` | Remove specific item |
| `.pop()` | Remove and return item |
| `.keys()` | Get dictionary keys |
| `.values()` | Get dictionary values |
| `.items()` | Get dictionary key-value pairs |

---

## Additional Resources

- [Python Official Documentation](https://docs.python.org/3/)
- [Python Tutorial](https://docs.python.org/3/tutorial/)
- [Python Standard Library](https://docs.python.org/3/library/)

---

## License

This code is provided for educational purposes.

---

## Contributing

Feel free to:
- Report issues
- Suggest improvements
- Add more examples
- Improve documentation

---

**Happy Learning! 🚀**
