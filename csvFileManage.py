import pandas as pd

# Load data from CSV file
df = pd.read_csv('/home/jerald/python/sample-python-projects/results.csv', skiprows=3)

# Display students with S grade in all subjects
students_with_s_grade = df[(df.iloc[:, 2:] == 'S').all(axis=1)][['REGISTER NO', 'NAME']]
print("Students with S grade in all subjects:")
print(students_with_s_grade)

# Compute pass percentage for each subject
subject_pass_percentages = (df.iloc[:, 2:] != 'F').mean() * 100
print("\nPass percentage for each subject:")
print(subject_pass_percentages)

# Display students who have passed all subjects
students_passed_all_subjects = df[(df.iloc[:, 2:] != 'F').all(axis=1)][['REGISTER NO', 'NAME']]
print("\nStudents who have passed all subjects:")
print(students_passed_all_subjects)





















# import pandas as pd

# data = [
#     ["REGISTER NO", "NAME", "CST301", "CST303", "CST305", "CST307", "CST309", "MCN301", "CSL31", "CSL33"],
#     ["PKD21CS001", "John Doe", "S", "A", "B", "C", "D", "F", "S", "S"],
#     ["PKD21CS002", "Jane Smith", "B", "B", "C", "D", "F", "S", "S", "S"],
#     ["PKD21CS003", "Alice Johnson", "S", "S", "S", "S", "S", "S", "S", "S"],
#     ["PKD21CS004", "Bob Brown", "A", "A", "A", "A", "A", "A", "A", "A"]
# ]

# # Create DataFrame from the provided data
# df = pd.DataFrame(data[1:], columns=data[0])

# # Display students with S grade in all subjects
# students_with_s_grade = df[df.iloc[:, 2:].eq('S').all(axis=1)][['REGISTER NO', 'NAME']]
# print("Students with S grade in all subjects:")
# print(students_with_s_grade)

# # Compute pass percentage for each subject
# subject_pass_percentages = df.iloc[:, 2:].apply(lambda x: (x != 'F').sum() / len(x) * 100)
# print("\nPass percentage for each subject:")
# print(subject_pass_percentages)

# # Display students who have passed all subjects
# students_passed_all_subjects = df[~df.iloc[:, 2:].eq('F').any(axis=1)][['REGISTER NO', 'NAME']]
# print("\nStudents who have passed all subjects:")
# print(students_passed_all_subjects)



# import pandas as pd

# # Specify the file path
# file_path = '/home/jerald/python/sample-python-projects/results.csv'

# # Read the CSV file into a DataFrame
# df = pd.read_csv(file_path)

# # Display the DataFrame
# print(df)
