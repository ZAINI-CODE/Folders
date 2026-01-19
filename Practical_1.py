name = "Alex"
roll_number = 101
cgpa = 3.8

print(name, roll_number, cgpa)

print(type(name))
print(type(roll_number))
print(type(cgpa))

student_name = input("Enter student's name: ")
marks_str1 = input("Enter marks for subject 1: ")
marks_str2 = input("Enter marks for subject 2: ")
marks_str3 = input("Enter marks for subject 3: ")

marks1 = int(marks_str1)
marks2 = int(marks_str2)
marks3 = int(marks_str3)

total_marks = marks1 + marks2 + marks3
average_marks = total_marks / 3

print(f"Total Marks: {total_marks}")
print(f"Average Marks: {average_marks:.2f}")

has_A = "A" in student_name
print(f"Does the name contain 'A'? {has_A}")

m1 = marks1
m2 = marks1
identity_check = m1 is m2
print(f"Identity check: {identity_check}")

single_quote_string = 'This is a string with single quotes.'
print(single_quote_string)

first_char = single_quote_string[0]
last_char = single_quote_string[-1]
print(f"First character: {first_char}")
print(f"Last character: {last_char}")

sliced_string = single_quote_string[0:4]
print(f"Sliced string: {sliced_string}")

string1 = "Artificial"
string2 = "Intelligence"
joined_string = string1 + " " + string2
print(joined_string)

num1 = 20
num2 = 5.5
print(f"Numeric addition: {num1 + num2}")

is_python_fun = True
print(f"Boolean value: {is_python_fun}")

integer_var = 10
float_var = 20.5
string_var = "Hello"
boolean_var = False

print(f"Type of {integer_var} is {type(integer_var)}")
print(f"Type of {float_var} is {type(float_var)}")
print(f"Type of '{string_var}' is {type(string_var)}")
print(f"Type of {boolean_var} is {type(boolean_var)}")
