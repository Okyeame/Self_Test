# Asking how many students
num_students = int(input("Enter number of students: "))

# Dictionary to store student data
students = {}

# Input names and scores
for i in range(num_students):
    name = input(f"Student {i+1} name: ")
    score = float(input(f"Score for {name}: "))

    # Grade assignment
    if score >= 80:
        grade = 'A'
    elif score >= 70:
        grade = 'B'
    elif score >= 60:
        grade = 'C'
    elif score >= 60:
        grade = 'C'
    elif score >= 50:
        grade = 'D'
    else:
        grade = 'F'

    # Store in dictionary
    students[name] = {'score' : score, 'grade' : grade}

# Step 4: Calculate class average and pass count
total_score = sum(student['score'] for student in students.values())
average = total_score / num_students
passed = sum(1 for student in students.values() if student['score'] >= 50)

# Step 5: Find top performer
top_student = max(students, key=lambda name: students[name]['score'])

# Step 6: Display results
print("\nResults:")
for name, data in students.items():
    print(f"{name} - {data['score']} - Grade {data['grade']}")

print(f"\nClass Average: {average:.2f}")
print(f"Students Passed: {passed}")
print(f"Top Performer: {top_student}")


