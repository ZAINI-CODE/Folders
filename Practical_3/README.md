# Practical 3: Dictionaries and Tuples in Python

This practical explores Python dictionaries, a powerful data structure for storing key-value pairs, and demonstrates nested dictionary operations.

## 📋 Tasks Overview

### Task 1: AI Patient Monitoring System
**File:** `task1_ai_patient_monitoring.py`

#### What You'll Learn:
- Creating and managing nested dictionaries
- Accessing dictionary keys, values, and items
- Dictionary and list comprehension
- Adding, updating, and removing dictionary entries
- Performing statistical calculations on dictionary data
- Conditional filtering of dictionary data

#### Data Structure:
```python
patients = {
    "P001": {
        "name": "John Doe",
        "conditions": ["Hypertension", "Diabetes"],
        "predictions": {"heart_risk": 0.75, "cancer_risk": 0.1}
    },
    "P002": {
        "name": "Alice Smith",
        "conditions": ["Asthma"],
        "predictions": {"heart_risk": 0.3, "diabetes_risk": 0.2}
    }
}
```

This creates a three-level nested structure:
- **Level 1:** Patient IDs as keys
- **Level 2:** Patient details (name, conditions, predictions)
- **Level 3:** Prediction metrics with risk values

#### Code Walkthrough:

**Accessing Dictionary Keys:**
```python
# Get all patient IDs
patient_ids = list(patients.keys())
# Output: ['P001', 'P002']
```

**Extracting Data with List Comprehension:**
```python
# Extract all patient names
patient_names = [details["name"] for details in patients.values()]
# Output: ['John Doe', 'Alice Smith']
```

**Iterating Through Dictionary:**
```python
# Loop through all patients and their details
for patient_id, details in patients.items():
    print(f"Patient ID: {patient_id}")
    print(f"Name: {details['name']}")
    print(f"Conditions: {details['conditions']}")
    print(f"Predictions: {details['predictions']}")
```

**Adding New Patient:**
```python
patients["P003"] = {
    "name": "Bob Johnson",
    "conditions": ["High Cholesterol"],
    "predictions": {"heart_risk": 0.6, "stroke_risk": 0.4}
}
```

**Updating Existing Data:**
```python
# Add a new condition to existing patient
patients["P001"]["conditions"].append("High Cholesterol")
```

**Statistical Calculations:**
```python
# Calculate average heart risk
heart_risks = []
for details in patients.values():
    if "heart_risk" in details["predictions"]:
        heart_risks.append(details["predictions"]["heart_risk"])

average_heart_risk = sum(heart_risks) / len(heart_risks)
```

**Conditional Filtering:**
```python
# Find all high-risk patients (heart_risk > 0.5)
high_risk_patients = []
for patient_id, details in patients.items():
    if "heart_risk" in details["predictions"]:
        if details["predictions"]["heart_risk"] > 0.5:
            high_risk_patients.append(details["name"])
```

**Dictionary Comprehension:**
```python
# Create name-to-ID mapping
name_to_id = {details["name"]: patient_id 
              for patient_id, details in patients.items()}
# Output: {'John Doe': 'P001', 'Alice Smith': 'P002'}
```

**Checking Membership:**
```python
if "P002" in patients:
    print(f"Patient exists: {patients['P002']['name']}")
```

**Removing Entries:**
```python
# Remove patient and get the removed data
removed_patient = patients.pop("P003", None)
if removed_patient:
    print(f"Removed: {removed_patient['name']}")
```

#### Expected Output:
```
Patient IDs: ['P001', 'P002']
Patient Names: ['John Doe', 'Alice Smith']

Patient ID: P001
Name: John Doe
Conditions: ['Hypertension', 'Diabetes']
Predictions: {'heart_risk': 0.75, 'cancer_risk': 0.1}

Patient ID: P002
Name: Alice Smith
Conditions: ['Asthma']
Predictions: {'heart_risk': 0.3, 'diabetes_risk': 0.2}

After adding new patient: {...}
Updated P001 conditions: ['Hypertension', 'Diabetes', 'High Cholesterol']
Average heart risk: 0.53
High risk patients (heart_risk > 0.5): ['John Doe', 'Bob Johnson']
Name to ID mapping: {'John Doe': 'P001', 'Alice Smith': 'P002', 'Bob Johnson': 'P003'}
Patient P002 exists: Alice Smith
Removed patient: Bob Johnson
```

---

## 🎯 Learning Objectives

By completing this practical, you will understand:

1. **Dictionary Basics** - Key-value pair structure
2. **Nested Dictionaries** - Dictionaries within dictionaries
3. **Dictionary Methods** - keys(), values(), items(), pop()
4. **Dictionary Comprehension** - Creating dictionaries efficiently
5. **List Comprehension with Dictionaries** - Extracting data
6. **Iterating Dictionaries** - Using items(), keys(), values()
7. **Data Manipulation** - Adding, updating, removing entries
8. **Statistical Operations** - Calculations on dictionary data
9. **Conditional Logic** - Filtering based on conditions

---

## 🚀 How to Run

1. Open a terminal/command prompt
2. Navigate to the Practical_3 directory:
   ```bash
   cd Practical_3
   ```
3. Run the task:
   ```bash
   python3 task1_ai_patient_monitoring.py
   ```

---

## 📝 Practice Exercises

Try these modifications:

1. **Add More Patients:**
   - Create 5 more patient records with different conditions
   - Include different prediction metrics

2. **Advanced Statistics:**
   - Find the patient with the highest heart risk
   - Calculate the average age if you add age field
   - Count total number of conditions across all patients

3. **Search Functionality:**
   - Find all patients with a specific condition
   - Search for patients by name
   - List all unique conditions

4. **Data Visualization:**
   - Sort patients by risk level
   - Group patients by condition
   - Create a summary report

---

## 🔑 Key Dictionary Concepts

### Creating Dictionaries:
```python
# Empty dictionary
my_dict = {}

# Dictionary with data
person = {"name": "John", "age": 30}

# Nested dictionary
company = {
    "employees": {
        "E001": {"name": "Alice", "role": "Engineer"},
        "E002": {"name": "Bob", "role": "Manager"}
    }
}
```

### Dictionary Methods:
| Method | Purpose | Returns |
|--------|---------|---------|
| `keys()` | Get all keys | dict_keys object |
| `values()` | Get all values | dict_values object |
| `items()` | Get key-value pairs | dict_items object |
| `get(key, default)` | Get value safely | Value or default |
| `pop(key, default)` | Remove and return | Value or default |
| `update(dict)` | Merge dictionaries | None |

### Accessing Values:
```python
# Direct access (raises error if key doesn't exist)
value = my_dict["key"]

# Safe access (returns None if key doesn't exist)
value = my_dict.get("key")

# Safe access with default
value = my_dict.get("key", "default_value")

# Nested access
value = my_dict["level1"]["level2"]["level3"]
```

### Adding/Updating:
```python
# Add new key-value pair
my_dict["new_key"] = "new_value"

# Update existing value
my_dict["existing_key"] = "updated_value"

# Add nested value
my_dict["key"]["nested_key"] = "value"
```

### Removing:
```python
# Remove and return value
value = my_dict.pop("key")

# Remove and return value with default
value = my_dict.pop("key", "not_found")

# Delete key-value pair
del my_dict["key"]

# Clear all items
my_dict.clear()
```

---

## ⚠️ Common Mistakes to Avoid

1. **KeyError - Accessing Non-existent Key:**
   ```python
   # Wrong:
   value = my_dict["nonexistent"]  # KeyError!
   
   # Correct:
   value = my_dict.get("nonexistent", "default")
   ```

2. **Modifying Dictionary While Iterating:**
   ```python
   # Problematic:
   for key in my_dict:
       del my_dict[key]  # Error!
   
   # Correct:
   for key in list(my_dict.keys()):
       del my_dict[key]
   ```

3. **Using Mutable Keys:**
   ```python
   # Wrong:
   my_dict = {[1, 2]: "value"}  # Lists can't be keys!
   
   # Correct:
   my_dict = {(1, 2): "value"}  # Tuples can be keys
   ```

4. **Not Checking for Key Existence:**
   ```python
   # Better practice:
   if "key" in my_dict:
       value = my_dict["key"]
   else:
       value = "default"
   
   # Or simply:
   value = my_dict.get("key", "default")
   ```

---

## 📚 Dictionary Comprehension Deep Dive

Dictionary comprehension creates dictionaries efficiently:

### Basic Syntax:
```python
new_dict = {key_expr: value_expr for item in iterable}
```

### Examples:
```python
# Create dictionary from two lists
keys = ['a', 'b', 'c']
values = [1, 2, 3]
my_dict = {k: v for k, v in zip(keys, values)}
# Result: {'a': 1, 'b': 2, 'c': 3}

# Square numbers
squares = {x: x**2 for x in range(5)}
# Result: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# Reverse a dictionary
reversed_dict = {v: k for k, v in original_dict.items()}

# Filter dictionary
filtered = {k: v for k, v in my_dict.items() if v > 10}
```

---

## 💡 Tips and Best Practices

1. **Use .get() for Safe Access:**
   ```python
   # Instead of:
   if "key" in my_dict:
       value = my_dict["key"]
   
   # Use:
   value = my_dict.get("key", default_value)
   ```

2. **Use .setdefault() for Default Values:**
   ```python
   # Adds key if it doesn't exist
   my_dict.setdefault("key", []).append("value")
   ```

3. **Iterate with .items() for Both Key and Value:**
   ```python
   for key, value in my_dict.items():
       print(f"{key}: {value}")
   ```

4. **Use Meaningful Keys:**
   ```python
   # Bad
   data = {1: "value", 2: "value"}
   
   # Good
   patient_data = {"patient_id": "P001", "name": "John"}
   ```

5. **Check Key Existence:**
   ```python
   if "key" in my_dict:
       # Key exists, safe to access
       value = my_dict["key"]
   ```

---

## 🔗 Dictionaries vs Other Data Structures

| Feature | List | Dictionary | Tuple | Set |
|---------|------|-----------|-------|-----|
| Ordered | ✓ (3.7+) | ✓ (3.7+) | ✓ | ✗ |
| Mutable | ✓ | ✓ | ✗ | ✓ |
| Indexed | By position | By key | By position | No |
| Duplicates | ✓ | Keys: ✗, Values: ✓ | ✓ | ✗ |
| Use case | Sequences | Key-value mapping | Immutable data | Unique items |

---

## 🌟 Real-World Applications

Dictionaries are used for:

1. **Configuration Files** - Storing settings and parameters
2. **Caching** - Storing computed results for quick lookup
3. **Counting** - Frequency of items
4. **Database Records** - Representing rows with named fields
5. **JSON Data** - Python dictionaries map directly to JSON
6. **API Responses** - Structured data from web services

---

## 📖 Additional Examples

### Counting with Dictionaries:
```python
# Count word frequency
words = ["apple", "banana", "apple", "orange", "banana", "apple"]
frequency = {}
for word in words:
    frequency[word] = frequency.get(word, 0) + 1
# Result: {'apple': 3, 'banana': 2, 'orange': 1}
```

### Grouping Data:
```python
# Group patients by disease
patients_by_disease = {}
for patient in patient_list:
    disease = patient["disease"]
    if disease not in patients_by_disease:
        patients_by_disease[disease] = []
    patients_by_disease[disease].append(patient["name"])
```

---

**Next:** Move to [Practical 4](../Practical_4/README.md) to learn about Functions and Modules!
