import csv
import json
import re

def clean_course_code(code):
    """Extract department and course number"""
    # Remove extra spaces and split
    code = code.strip().upper()
    match = re.match(r'([A-Z]+)\s*(\d+)', code)
    if match:
        dept = match.group(1)
        num = match.group(2)
        return f"{dept}{num}", dept
    return code, code[:4]

reviews = []
with open('class review.csv', 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        course_code, dept = clean_course_code(row['Course code'])
        
        reviews.append({
            'courseCode': course_code,
            'department': dept,
            'professor': row['Professor'].strip(),
            'review': row['How did you feel about the class?'].strip(),
            'rating': int(row['Out of 5']) if row['Out of 5'].strip() else 3
        })

# Create data directory if it doesn't exist
import os
os.makedirs('data', exist_ok=True)

with open('data/reviews.json', 'w', encoding='utf-8') as f:
    json.dump(reviews, f, ensure_ascii=False, indent=2)

print(f"✅ Converted {len(reviews)} reviews to data/reviews.json")