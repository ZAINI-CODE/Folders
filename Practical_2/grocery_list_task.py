"""
Practical 2: Implementing Data Structures List and Set
Grocery List Task: List Operations

This program demonstrates:
- List creation
- extend() method to add multiple items
- insert() method to add items at specific positions
- remove() method to delete items
- index() method to find position of items
- List slicing
"""

# Create initial grocery list
grocery_list = ['Apples', 'Bananas', 'Carrots']

# Add multiple items using extend()
other_items = ['Milk', 'Bread']
grocery_list.extend(other_items)

# Insert items at specific positions
grocery_list.insert(1, 'Tomatoes')  # Insert at index 1
grocery_list.insert(2, 'Lettuce')  # Insert at index 2
print(f"List after adding items: {grocery_list}")

# Remove an item from the list
grocery_list.remove('Bananas')
print(f"List after removing Bananas: {grocery_list}")

# Find index of an item and slice from that position
start_index = grocery_list.index('Tomatoes')
final_slice = grocery_list[start_index:]
print(f"Final Slice: {final_slice}")
