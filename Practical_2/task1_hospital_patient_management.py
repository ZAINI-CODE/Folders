"""
Practical 2: Implementing Data Structures List and Set
Task 1: Hospital Patient Management System

This program demonstrates:
- Creating and managing nested lists (2D lists)
- append() method to add new patient records
- insert() method to add records at specific positions
- extend() method to add multiple records
- Removing specific records by searching
- pop() method to remove items from specific positions
- List comprehension to extract specific data
- Sorting lists
- copy() method for creating independent list copies
- Accessing elements using positive and negative indexing
- Updating nested list elements
"""

# Create initial patient list with nested lists
# Each patient record: [ID, Name, Age, Disease]
patients = [
    [101, "Ali", 25, "Flu"],
    [102, "Sara", 30, "Fever"],
    [103, "Ahmed", 40, "Diabetes"],
    [104, "Fatima", 22, "Flu"],
    [105, "Zain", 35, "Cold"]
]
print(f"Initial patient list: {patients}")

# Add a new patient using append()
patients.append([106, "Hina", 50, "Headache"])
print(f"After appending: {patients}")

# Insert a new patient at specific position (index 3)
patients.insert(3, [107, "Hassan", 28, "Cough"])
print(f"After inserting: {patients}")

# Add multiple patients using extend()
new_patients = [[108, "Bilal", 45, "Allergy"], [109, "Ayesha", 33, "Fever"]]
patients.extend(new_patients)
print(f"After extending: {patients}")

# Remove a specific patient (ID 103)
patient_to_remove = None
for patient in patients:
    if patient[0] == 103:
        patient_to_remove = patient
        break

if patient_to_remove:
    patients.remove(patient_to_remove)
print(f"After removing patient 103: {patients}")

# Remove and return the last patient using pop()
discharged_patient = patients.pop()
print(f"Discharged last patient: {discharged_patient}")

# Remove and return patient at specific index using pop(index)
third_patient_discharged = patients.pop(2)
print(f"Discharged third patient: {third_patient_discharged}")

# After popping operations
print(f"List after popping: {patients}")

# Count patients with specific disease (Flu)
flu_count = 0
for patient in patients:
    if patient[3] == "Flu":
        flu_count += 1
print(f"Number of patients with Flu: {flu_count}")

# Extract all ages using list comprehension and sort them
ages = [patient[2] for patient in patients]
ages.sort()  # Sort in ascending order
print(f"Ages sorted ascending: {ages}")

ages.reverse()  # Reverse to get descending order
print(f"Ages sorted descending: {ages}")

# Create a backup copy of patients list
backup_patients = patients.copy()
backup_patients.append([110, "Saad", 19, "Injury"])
print(f"Original list is different: {patients}")
print(f"Backup list is different: {backup_patients}")

# Access specific elements using indexing
print(f"Name of second patient: {patients[1][1]}")  # Index 1, element 1 (name)
print(f"Disease of last patient: {patients[-1][3]}")  # Last patient, disease

# Update a patient's disease
for patient in patients:
    if patient[1] == "Sara":
        patient[3] = "High Fever"
print(f"Updated patient list: {patients}")
