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

print("Patient IDs:", list(patients.keys()))

patient_names = [details["name"] for details in patients.values()]
print("Patient Names:", patient_names)

for patient_id, details in patients.items():
    print(f"\nPatient ID: {patient_id}")
    print(f"Name: {details['name']}")
    print(f"Conditions: {details['conditions']}")
    print(f"Predictions: {details['predictions']}")

patients["P003"] = {
    "name": "Bob Johnson",
    "conditions": ["High Cholesterol"],
    "predictions": {"heart_risk": 0.6, "stroke_risk": 0.4}
}
print(f"\nAfter adding new patient: {patients}")

patients["P001"]["conditions"].append("High Cholesterol")
print(f"\nUpdated P001 conditions: {patients['P001']['conditions']}")

heart_risks = []
for details in patients.values():
    if "heart_risk" in details["predictions"]:
        heart_risks.append(details["predictions"]["heart_risk"])

if heart_risks:
    average_heart_risk = sum(heart_risks) / len(heart_risks)
    print(f"\nAverage heart risk: {average_heart_risk:.2f}")

high_risk_patients = []
for patient_id, details in patients.items():
    if "heart_risk" in details["predictions"]:
        if details["predictions"]["heart_risk"] > 0.5:
            high_risk_patients.append(details["name"])

print(f"High risk patients (heart_risk > 0.5): {high_risk_patients}")

name_to_id = {details["name"]: patient_id for patient_id, details in patients.items()}
print(f"\nName to ID mapping: {name_to_id}")

if "P002" in patients:
    print(f"\nPatient P002 exists: {patients['P002']['name']}")

removed_patient = patients.pop("P003", None)
if removed_patient:
    print(f"\nRemoved patient: {removed_patient['name']}")

print(f"\nFinal patient dictionary: {patients}")
