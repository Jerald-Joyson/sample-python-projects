import csv

# Data provided
data = [
    ["REGISTER NO", "NAME", "CST301", "CST303", "CST305", "CST307", "CST309", "MCN301", "CSL31", "CSL33"],
    ["PKD21CS001", "John Doe", "S", "A", "B", "C", "D", "F", "S", "S"],
    ["PKD21CS002", "Jane Smith", "B", "B", "C", "D", "F", "S", "S", "S"],
    ["PKD21CS003", "Alice Johnson", "S", "S", "S", "S", "S", "S", "S", "S"],
    ["PKD21CS004", "Bob Brown", "A", "A", "A", "A", "A", "A", "A", "A"]
]

# File path to save the CSV
csv_file_path = "student_data.csv"

# Write data to CSV file
with open(csv_file_path, "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(data)

print(f"Data has been written to {csv_file_path}")
