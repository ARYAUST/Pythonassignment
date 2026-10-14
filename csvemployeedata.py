import csv

with open("employees.csv", "w", newline="") as file:
    writer = csv.writer(file)

    # Column headers
    writer.writerow(["id", "name", "salary"])

    # Employee records
    writer.writerow([1, "Arya", 50000])
    writer.writerow([2, "Sree", 45000])
    writer.writerow([3, "Niha", 55000])

print("employees.csv created successfully.")