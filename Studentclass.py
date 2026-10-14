class Student:
    # Constructor
    def __init__(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks

    # Method to display details
    def display_details(self):
        print("Name:", self.name)
        print("Roll No:", self.roll_no)
        print("Marks:", self.marks)

    # Method to check result
    def check_result(self):
        if self.marks >= 40:
            return "Pass"
        else:
            return "Fail"


# Creating three objects
student1 = Student("Arya", 101, 76)
student2 = Student("Sree", 102, 34)
student3 = Student("Niha", 103, 45)

# Display details and results
for student in [student1, student2, student3]:
    student.display_details()
    print("Result:", student.check_result())
    print("-" * 20)