"""
Practical 1: Python Variables, Datatypes and Operators
Task 3: String Operations and Type Demonstrations

This program demonstrates:
- String indexing (accessing first and last characters)
- String slicing
- String concatenation
- Arithmetic operations with mixed data types
- Boolean variables
- Type checking for different data types
"""

# String operations - indexing and slicing
single_quote_string = 'This is a string with single quotes.'
print(single_quote_string)

# Access first and last character using indexing
first_char = single_quote_string[0]
last_char = single_quote_string[-1]
print(f"First character: {first_char}")
print(f"Last character: {last_char}")

# String slicing - extract substring from index 0 to 4
sliced_string = single_quote_string[0:4]
print(f"Sliced string: {sliced_string}")

# String concatenation
string1 = "Artificial"
string2 = "Intelligence"
joined_string = string1 + " " + string2
print(joined_string)

# Numeric operations with different data types
num1 = 20  # Integer
num2 = 5.5  # Float
print(f"Numeric addition: {num1 + num2}")

# Boolean variable
is_python_fun = True
print(f"Boolean value: {is_python_fun}")

# Type checking for different data types
integer_var = 10
float_var = 20.5
string_var = "Hello"
boolean_var = False

print(f"Type of {integer_var} is {type(integer_var)}")
print(f"Type of {float_var} is {type(float_var)}")
print(f"Type of '{string_var}' is {type(string_var)}")
print(f"Type of {boolean_var} is {type(boolean_var)}")
