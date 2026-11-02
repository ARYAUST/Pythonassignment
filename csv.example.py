import csv

with open("employees.csv", "w", newline="") as file:
    writer = csv.writer(file)

    # Column headers
    writer.writerow(["id", "name", "salary"])

print("employees.csv created successfully.")