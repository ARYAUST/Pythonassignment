# Create and write to the file
with open("notes.txt", "w") as file:
    file.write("Python is easy to learn.\n")
    file.write("File handling is important.\n")
    file.write("This is the third line.\n")
    file.write("Practice makes perfect.\n")
    file.write("Keep learning every day.\n")

# Read and print the complete file
print("Complete File Content:")
with open("notes.txt", "r") as file:
    print(file.read())

# Print only the third line
with open("notes.txt", "r") as file:
    lines = file.readlines()
    print("Third Line:")
    print(lines[2])  # Index 2 = third line

# Append one more line
with open("notes.txt", "a") as file:
    file.write("This line was appended later.\n")

# Display updated file contents
print("Updated File Content:")
with open("notes.txt", "r") as file:
    print(file.read())