students = {
    "Arya": 76,
    "Sree": 34,
    "Niha": 45
}

for name, marks in students.items():
    if marks >= 40:
        print(name, "-", marks, "- Pass")
    else:
        print(name, "-", marks, "- Fail")