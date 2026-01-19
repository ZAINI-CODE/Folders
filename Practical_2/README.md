# Practical 2: Implementing Data Structures - List and Set

This practical focuses on Python lists, one of the most versatile and commonly used data structures in Python.

## 📋 Tasks Overview

### Grocery List Task
**File:** `grocery_list_task.py`

#### What You'll Learn:
- Creating and initializing lists
- Adding items to lists using different methods
- Removing items from lists
- Finding the position of items
- Slicing lists to extract portions

#### Code Walkthrough:
```python
# Create initial list
grocery_list = ['Apples', 'Bananas', 'Carrots']

# Add multiple items at once
other_items = ['Milk', 'Bread']
grocery_list.extend(other_items)

# Insert at specific position
grocery_list.insert(1, 'Tomatoes')  # Insert at index 1

# Remove specific item
grocery_list.remove('Bananas')

# Find position and slice from there
start_index = grocery_list.index('Tomatoes')
final_slice = grocery_list[start_index:]
```

#### Key List Methods:
- **`extend(list)`** - Add all items from another list
- **`insert(index, item)`** - Add item at specific position
- **`remove(item)`** - Remove first occurrence of item
- **`index(item)`** - Find position of item

#### Expected Output:
```
List after adding items: ['Apples', 'Tomatoes', 'Lettuce', 'Bananas', 'Carrots', 'Milk', 'Bread']
List after removing Bananas: ['Apples', 'Tomatoes', 'Lettuce', 'Carrots', 'Milk', 'Bread']
Final Slice: ['Tomatoes', 'Lettuce', 'Carrots', 'Milk', 'Bread']
```

---

### Task 1: Hospital Patient Management System
**File:** `task1_hospital_patient_management.py`

#### What You'll Learn:
- Working with nested lists (2D lists)
- Multiple ways to add items to lists
- Different methods to remove items
- List comprehension for efficient data extraction
- Sorting and reversing lists
- Creating independent copies of lists
- Accessing and updating nested list elements

#### Data Structure:
```python
patients = [
    [101, "Ali", 25, "Flu"],      # [ID, Name, Age, Disease]
    [102, "Sara", 30, "Fever"],
    # ... more patients
]
```

#### Code Walkthrough:

**Adding Patients:**
```python
# Method 1: append() - Add one patient at the end
patients.append([106, "Hina", 50, "Headache"])

# Method 2: insert() - Add at specific position
patients.insert(3, [107, "Hassan", 28, "Cough"])

# Method 3: extend() - Add multiple patients
new_patients = [[108, "Bilal", 45, "Allergy"], [109, "Ayesha", 33, "Fever"]]
patients.extend(new_patients)
```

**Removing Patients:**
```python
# Method 1: remove() - Remove specific patient by searching
for patient in patients:
    if patient[0] == 103:  # Find patient with ID 103
        patients.remove(patient)

# Method 2: pop() - Remove and return last patient
discharged_patient = patients.pop()

# Method 3: pop(index) - Remove patient at specific position
third_patient = patients.pop(2)
```

**List Comprehension:**
```python
# Extract all ages from patient records
ages = [patient[2] for patient in patients]
```

**Sorting:**
```python
ages.sort()      # Sort in ascending order
ages.reverse()   # Reverse to get descending order
```

**Creating Independent Copies:**
```python
# Create a copy that won't affect the original
backup_patients = patients.copy()
backup_patients.append([110, "Saad", 19, "Injury"])
# Original list remains unchanged
```

**Accessing Nested Elements:**
```python
# Access name of second patient
name = patients[1][1]

# Access disease of last patient
disease = patients[-1][3]
```

**Updating Nested Elements:**
```python
# Find Sara and update her disease
for patient in patients:
    if patient[1] == "Sara":
        patient[3] = "High Fever"
```

#### Expected Output:
```
Initial patient list: [[101, 'Ali', 25, 'Flu'], [102, 'Sara', 30, 'Fever'], ...]
After appending: [[101, 'Ali', 25, 'Flu'], ..., [106, 'Hina', 50, 'Headache']]
After inserting: [[101, 'Ali', 25, 'Flu'], ..., [107, 'Hassan', 28, 'Cough'], ...]
...
Number of patients with Flu: 2
Ages sorted ascending: [22, 25, 28, 30, 45, 50]
Ages sorted descending: [50, 45, 30, 28, 25, 22]
Name of second patient: Sara
Disease of last patient: Fever
Updated patient list: [... with Sara's disease updated to "High Fever"]
```

---

## 🎯 Learning Objectives

By completing this practical, you will understand:

1. **List Creation** - How to create and initialize lists
2. **List Methods** - append(), insert(), extend(), remove(), pop()
3. **List Comprehension** - Efficient way to create new lists
4. **Nested Lists** - Lists within lists (2D structures)
5. **List Operations** - Sorting, reversing, copying
6. **Indexing** - Accessing elements with positive and negative indices
7. **Slicing** - Extracting portions of lists

---

## 🚀 How to Run

1. Open a terminal/command prompt
2. Navigate to the Practical_2 directory:
   ```bash
   cd Practical_2
   ```
3. Run each task:
   ```bash
   python3 grocery_list_task.py
   python3 task1_hospital_patient_management.py
   ```

---

## 📝 Practice Exercises

Try these modifications:

1. **Grocery List:**
   - Add more items to the initial list
   - Try removing items that don't exist (handle the error)
   - Create a sorted version of the list

2. **Hospital Management:**
   - Add a function to find all patients with a specific disease
   - Calculate the average age of patients
   - Sort patients by age or ID

---

## 🔑 Key List Concepts

### List Creation:
```python
# Empty list
my_list = []

# List with items
fruits = ['apple', 'banana', 'orange']

# Nested list
matrix = [[1, 2], [3, 4], [5, 6]]
```

### Adding Items:
| Method | Purpose | Example |
|--------|---------|---------|
| `append(item)` | Add one item to end | `list.append('x')` |
| `insert(index, item)` | Add at position | `list.insert(0, 'x')` |
| `extend(list)` | Add multiple items | `list.extend(['x', 'y'])` |

### Removing Items:
| Method | Purpose | Returns |
|--------|---------|---------|
| `remove(item)` | Remove first match | None |
| `pop()` | Remove last item | Removed item |
| `pop(index)` | Remove at index | Removed item |

### Accessing Items:
```python
list[0]      # First item
list[-1]     # Last item
list[1:3]    # Items from index 1 to 2
list[::2]    # Every other item
```

### Useful Methods:
- `list.index(item)` - Find position of item
- `list.sort()` - Sort in place
- `list.reverse()` - Reverse in place
- `list.copy()` - Create independent copy
- `list.count(item)` - Count occurrences

---

## ⚠️ Common Mistakes to Avoid

1. **Modifying Original List When You Don't Want To:**
   ```python
   # Wrong:
   backup = original_list  # Both point to same list!
   
   # Correct:
   backup = original_list.copy()  # Independent copy
   ```

2. **Index Out of Range:**
   ```python
   my_list = [1, 2, 3]
   print(my_list[5])  # Error! Only indices 0-2 exist
   ```

3. **Removing While Iterating:**
   ```python
   # Problematic:
   for item in my_list:
       my_list.remove(item)  # Can skip items!
   
   # Better:
   my_list.clear()  # Or create new list
   ```

4. **Confusing append() and extend():**
   ```python
   list1 = [1, 2]
   list1.append([3, 4])     # Result: [1, 2, [3, 4]]
   
   list2 = [1, 2]
   list2.extend([3, 4])     # Result: [1, 2, 3, 4]
   ```

---

## 📚 List Comprehension Deep Dive

List comprehension is a concise way to create lists:

### Basic Syntax:
```python
new_list = [expression for item in iterable]
```

### Examples:
```python
# Extract ages from patients
ages = [patient[2] for patient in patients]

# Create list of squares
squares = [x**2 for x in range(10)]

# Filter even numbers
evens = [x for x in range(10) if x % 2 == 0]

# Transform strings to uppercase
names = [name.upper() for name in patient_names]
```

---

## 💡 Tips and Best Practices

1. **Use meaningful variable names:**
   ```python
   # Bad
   l = [1, 2, 3]
   
   # Good
   patient_ids = [101, 102, 103]
   ```

2. **Use list comprehension for simple transformations:**
   ```python
   # Instead of:
   ages = []
   for patient in patients:
       ages.append(patient[2])
   
   # Use:
   ages = [patient[2] for patient in patients]
   ```

3. **Check before removing:**
   ```python
   if item in my_list:
       my_list.remove(item)
   ```

4. **Use negative indexing for end access:**
   ```python
   last_item = my_list[-1]
   second_last = my_list[-2]
   ```

---

## 🔗 Related Concepts

- **Tuples:** Immutable version of lists
- **Sets:** Unordered collection of unique items
- **Dictionaries:** Key-value pairs for structured data

---

**Next:** Move to [Practical 3](../Practical_3/README.md) to learn about Dictionaries and Tuples!
