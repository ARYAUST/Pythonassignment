# Function to calculate grade
def calculate_grade(avg):
    if avg >= 75:
        return "A"
    elif avg >= 60:
        return "B"
    elif avg >= 40:
        return "C"
    else:
        return "F"


# Student data stored in a list of dictionaries
students = [
    {"id": 101, "name": "Rahul", "python": 80, "sql": 78, "ai": 82},
    {"id": 102, "name": "Anjali", "python": 65, "sql": 60, "ai": 70},
    {"id": 103, "name": "Priya", "python": 90, "sql": 85, "ai": 88},
    {"id": 104, "name": "Amit", "python": 35, "sql": 40, "ai": 30}
]

# Calculate results
for student in students:
    total = student["python"] + student["sql"] + student["ai"]
    average = total / 3

    student["total"] = total
    student["average"] = average
    student["grade"] = calculate_grade(average)
    student["result"] = "PASS" if average >= 40 else "FAIL"

# Display all student details
print("=" * 25)
print("===== Student Result =====")
print("=" * 25)

for student in students:
    print(f"\nStudent ID: {student['id']}")
    print(f"Name: {student['name']}")
    print(f"Total: {student['total']}")
    print(f"Average: {student['average']:.2f}")
    print(f"Grade: {student['grade']}")
    print(f"Result: {student['result']}")

# Highest average student
highest_student = max(students, key=lambda x: x["average"])

print("\n" + "=" * 25)
print(f"Highest Scoring Student: {highest_student['name']}")

# List comprehension
above_75 = [student["name"] for student in students if student["average"] > 75]

print("Students above 75:", ", ".join(above_75))