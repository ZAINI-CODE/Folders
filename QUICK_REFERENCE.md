# Python Quick Reference Guide

This guide provides quick references to all concepts covered in the practicals.

## Table of Contents
1. [Variables and Data Types](#variables-and-data-types)
2. [Operators](#operators)
3. [Lists](#lists)
4. [Dictionaries](#dictionaries)
5. [Functions](#functions)
6. [Common Patterns](#common-patterns)

---

## Variables and Data Types

### Variable Declaration
```python
name = "Alex"           # String
age = 25                # Integer
height = 5.9            # Float
is_student = True       # Boolean
```

### Type Checking
```python
type(name)              # <class 'str'>
type(age)               # <class 'int'>
```

### Type Conversion
```python
int("123")              # String to integer
float("3.14")           # String to float
str(123)                # Integer to string
```

---

## Operators

### Arithmetic Operators
```python
a + b                   # Addition
a - b                   # Subtraction
a * b                   # Multiplication
a / b                   # Division
a // b                  # Floor division
a % b                   # Modulus
a ** b                  # Power
```

### Comparison Operators
```python
a == b                  # Equal
a != b                  # Not equal
a > b                   # Greater than
a < b                   # Less than
a >= b                  # Greater than or equal
a <= b                  # Less than or equal
```

### Membership Operators
```python
"A" in string           # Check if 'A' is in string
item in list            # Check if item is in list
key in dict             # Check if key is in dictionary
```

### Identity Operators
```python
a is b                  # Same object
a is not b              # Different objects
```

---

## Lists

### Creating Lists
```python
empty_list = []
fruits = ['apple', 'banana', 'orange']
nested = [[1, 2], [3, 4]]
```

### Adding Items
```python
list.append(item)              # Add to end
list.insert(index, item)       # Insert at position
list.extend([item1, item2])    # Add multiple items
```

### Removing Items
```python
list.remove(item)              # Remove first match
item = list.pop()              # Remove and return last
item = list.pop(index)         # Remove at index
list.clear()                   # Remove all items
```

### Accessing Items
```python
list[0]                        # First item
list[-1]                       # Last item
list[1:3]                      # Items from 1 to 2
list[::2]                      # Every other item
```

### List Operations
```python
len(list)                      # Length
list.sort()                    # Sort in place
list.reverse()                 # Reverse in place
list.index(item)               # Find position
list.count(item)               # Count occurrences
new_list = list.copy()         # Create copy
```

### List Comprehension
```python
# Basic syntax
[expression for item in list]

# Examples
squares = [x**2 for x in range(10)]
evens = [x for x in range(10) if x % 2 == 0]
names = [person['name'] for person in people]
```

---

## Dictionaries

### Creating Dictionaries
```python
empty_dict = {}
person = {"name": "John", "age": 30}
nested = {"users": {"u1": {"name": "Alice"}}}
```

### Accessing Values
```python
dict["key"]                    # Direct access (may raise error)
dict.get("key")                # Safe access (returns None)
dict.get("key", "default")     # Safe with default
```

### Adding/Updating
```python
dict["new_key"] = value        # Add or update
dict.update({"k1": "v1"})      # Merge dictionaries
```

### Removing
```python
value = dict.pop("key")        # Remove and return
value = dict.pop("key", None)  # Safe remove
del dict["key"]                # Delete key-value
dict.clear()                   # Remove all
```

### Dictionary Methods
```python
dict.keys()                    # Get all keys
dict.values()                  # Get all values
dict.items()                   # Get key-value pairs
```

### Iterating
```python
# Iterate keys
for key in dict:
    print(key)

# Iterate values
for value in dict.values():
    print(value)

# Iterate key-value pairs
for key, value in dict.items():
    print(f"{key}: {value}")
```

### Dictionary Comprehension
```python
# Basic syntax
{key_expr: value_expr for item in list}

# Examples
squares = {x: x**2 for x in range(5)}
filtered = {k: v for k, v in dict.items() if v > 10}
reversed_dict = {v: k for k, v in dict.items()}
```

---

## Functions

### Basic Function
```python
def function_name(parameter):
    """Docstring describing function"""
    # Function body
    return value
```

### Function Types
```python
# No parameters, no return
def greet():
    print("Hello!")

# With parameters
def greet(name):
    print(f"Hello, {name}!")

# With return value
def add(a, b):
    return a + b

# With default parameters
def greet(name="Guest"):
    print(f"Hello, {name}!")

# Multiple return values
def get_min_max(numbers):
    return min(numbers), max(numbers)
```

### Lambda Functions
```python
# Basic syntax
lambda parameters: expression

# Examples
square = lambda x: x ** 2
add = lambda a, b: a + b

# With sorted
students.sort(key=lambda s: s['name'])
```

---

## Common Patterns

### Input from User
```python
name = input("Enter name: ")
age = int(input("Enter age: "))
marks = float(input("Enter marks: "))
```

### String Formatting
```python
# f-strings (Python 3.6+)
print(f"Name: {name}, Age: {age}")

# format() method
print("Name: {}, Age: {}".format(name, age))

# % operator
print("Name: %s, Age: %d" % (name, age))
```

### Loop Patterns
```python
# For loop
for item in list:
    print(item)

# While loop
while condition:
    # code

# Range
for i in range(10):         # 0 to 9
    print(i)

for i in range(5, 10):      # 5 to 9
    print(i)

for i in range(0, 10, 2):   # 0, 2, 4, 6, 8
    print(i)
```

### Conditional Statements
```python
if condition:
    # code
elif condition:
    # code
else:
    # code
```

### Menu-Driven Program
```python
while True:
    print("1. Option 1")
    print("2. Option 2")
    print("3. Exit")
    
    choice = input("Enter choice: ")
    
    if choice == '1':
        # Handle option 1
    elif choice == '2':
        # Handle option 2
    elif choice == '3':
        break
    else:
        print("Invalid choice")
```

### Finding in List
```python
# Find item
for item in list:
    if item == target:
        found = item
        break

# Find in nested list
for item in nested_list:
    if item[0] == target:
        found = item
        break
```

### Calculate Statistics
```python
# Sum
total = sum(numbers)

# Average
average = sum(numbers) / len(numbers)

# Maximum
maximum = max(numbers)

# Minimum
minimum = min(numbers)

# Count
count = numbers.count(value)
```

### String Operations
```python
string[0]                      # First character
string[-1]                     # Last character
string[0:4]                    # Slice (0 to 3)
string.upper()                 # Uppercase
string.lower()                 # Lowercase
string.split()                 # Split into list
" ".join(list)                 # Join list into string
string.replace("old", "new")   # Replace
string.strip()                 # Remove whitespace
```

---

## Error Handling

### Try-Except
```python
try:
    # Code that might raise error
    value = int(input("Enter number: "))
except ValueError:
    print("Invalid number!")
except Exception as e:
    print(f"Error: {e}")
finally:
    print("This always runs")
```

---

## File Operations

### Reading Files
```python
# Read entire file
with open('file.txt', 'r') as f:
    content = f.read()

# Read line by line
with open('file.txt', 'r') as f:
    for line in f:
        print(line)
```

### Writing Files
```python
# Write (overwrite)
with open('file.txt', 'w') as f:
    f.write("Hello\n")

# Append
with open('file.txt', 'a') as f:
    f.write("World\n")
```

---

## Useful Built-in Functions

```python
len(sequence)                  # Length
range(start, stop, step)       # Generate sequence
enumerate(list)                # Index and value
zip(list1, list2)              # Combine lists
sorted(list)                   # Return sorted copy
reversed(list)                 # Return reversed iterator
all(list)                      # All True?
any(list)                      # Any True?
sum(numbers)                   # Sum of numbers
min(numbers)                   # Minimum
max(numbers)                   # Maximum
abs(number)                    # Absolute value
round(number, digits)          # Round number (digits optional, defaults to 0)
```

---

## Best Practices

1. **Use meaningful variable names**
   ```python
   # Bad
   x = 5
   
   # Good
   student_age = 5
   ```

2. **Add comments for clarity**
   ```python
   # Calculate average marks
   average = total / count
   ```

3. **Use docstrings for functions**
   ```python
   def calculate_grade(marks):
       """Calculate letter grade from marks."""
       pass
   ```

4. **Handle errors gracefully**
   ```python
   if key in dict:
       value = dict[key]
   ```

5. **Use list/dict comprehension for simple operations**
   ```python
   # Good
   squares = [x**2 for x in range(10)]
   ```

---

**For more details, refer to the individual practical README files!**
