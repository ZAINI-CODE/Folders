grocery_list = ['Apples', 'Bananas', 'Carrots']

other_items = ['Milk', 'Bread']
grocery_list.extend(other_items)

grocery_list.insert(1, 'Tomatoes')
grocery_list.insert(2, 'Lettuce')
print(f"List after adding items: {grocery_list}")

grocery_list.remove('Bananas')
print(f"List after removing Bananas: {grocery_list}")

start_index = grocery_list.index('Tomatoes')
final_slice = grocery_list[start_index:]
print(f"Final Slice: {final_slice}")

patients = [
    [101, "Ali", 25, "Flu"],
    [102, "Sara", 30, "Fever"],
    [103, "Ahmed", 40, "Diabetes"],
    [104, "Fatima", 22, "Flu"],
    [105, "Zain", 35, "Cold"]
]
print(f"Initial patient list: {patients}")

patients.append([106, "Hina", 50, "Headache"])
print(f"After appending: {patients}")

patients.insert(3, [107, "Hassan", 28, "Cough"])
print(f"After inserting: {patients}")

new_patients = [[108, "Bilal", 45, "Allergy"], [109, "Ayesha", 33, "Fever"]]
patients.extend(new_patients)
print(f"After extending: {patients}")

patient_to_remove = None
for patient in patients:
    if patient[0] == 103:
        patient_to_remove = patient
        break

if patient_to_remove:
    patients.remove(patient_to_remove)
print(f"After removing patient 103: {patients}")

discharged_patient = patients.pop()
print(f"Discharged last patient: {discharged_patient}")

third_patient_discharged = patients.pop(2)
print(f"Discharged third patient: {third_patient_discharged}")

print(f"List after popping: {patients}")

flu_count = 0
for patient in patients:
    if patient[3] == "Flu":
        flu_count += 1
print(f"Number of patients with Flu: {flu_count}")

ages = [patient[2] for patient in patients]
ages.sort()
print(f"Ages sorted ascending: {ages}")

ages.reverse()
print(f"Ages sorted descending: {ages}")

backup_patients = patients.copy()
backup_patients.append([110, "Saad", 19, "Injury"])
print(f"Original list is different: {patients}")
print(f"Backup list is different: {backup_patients}")

print(f"Name of second patient: {patients[1][1]}")
print(f"Disease of last patient: {patients[-1][3]}")

for patient in patients:
    if patient[1] == "Sara":
        patient[3] = "High Fever"
print(f"Updated patient list: {patients}")
