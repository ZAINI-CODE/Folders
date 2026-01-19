def analyze_text(text):
    counts = {'uppercase': 0, 'lowercase': 0, 'digits': 0}
    for char in text:
        if char.isupper():
            counts['uppercase'] += 1
        elif char.islower():
            counts['lowercase'] += 1
        elif char.isdigit():
            counts['digits'] += 1
    return counts

sample_text = "Pen2PDF is the #1 Productivity Suite in 2024!"
analysis_result = analyze_text(sample_text)
print(analysis_result)

def reverse_word_order(sentence):
    words = sentence.split()
    reversed_sentence = ' '.join(words[::-1])
    return reversed_sentence

input_sentence = 'Artificial Intelligence Lab'
output_sentence = reverse_word_order(input_sentence)
print(output_sentence)

def analyze_traffic():
    traffic_data = {
        'Intersection 1': {'Morning': 120, 'Afternoon': 75, 'Evening': 150},
        'Intersection 2': {'Morning': 45, 'Afternoon': 90, 'Evening': 60},
        'Intersection 3': {'Morning': 80, 'Afternoon': 85, 'Evening': 110}
    }
    
    print("Traffic Congestion Summary Report")
    print("-" * 35)
    
    for intersection, data in traffic_data.items():
        print(f"{intersection}:")
        for period, cars in data.items():
            level = ''
            if cars > 100:
                level = 'High'
            elif cars >= 50:
                level = 'Medium'
            else:
                level = 'Low'
            print(f"  - {period}: {cars} cars (Congestion: {level})")
        print()

analyze_traffic()
