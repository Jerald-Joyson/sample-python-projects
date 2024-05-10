






import pandas as pd

# Read the CSV file
df = pd.read_csv('results.csv')

# Task 1: Display students with an 'S' grade in all subjects
s_grade_students = df[(df['CST301'] == 'S') &
                      (df['CST303'] == 'S') &
                      (df['CST305'] == 'S') &
                      (df['CST307'] == 'S') &
                      (df['CST309'] == 'S') &
                      (df['MNC301'] == 'S') &
                      (df['CSL 331'] == 'S') &
                      (df['CSL 333'] == 'S')]

print("Students with 'S' grade in all subjects:")
print(s_grade_students[['REGISTER NO', 'NAME']])

# Task 2: Compute pass percentage for each subject
pass_percentage = {}
for subject in ['CST301', 'CST303', 'CST305', 'CST307', 'CST309', 'MNC301', 'CSL 331', 'CSL 333']:
    # Calculate pass percentage for each subject
    pass_percentage[subject] = (df[subject].value_counts(normalize=True) * 100).get('S', 0)

print("\nPass percentage for each subject:")
for subject, percentage in pass_percentage.items():
    print(f"{subject}: {percentage:.2f}%")

# Task 3: Display students who have passed all subjects
passed_all_subjects = df[(df['CST301'] == 'S') &
                         (df['CST303'] == 'S') &
                         (df['CST305'] == 'S') &
                         (df['CST307'] == 'S') &
                         (df['CST309'] == 'S') &
                         (df['MNC301'] == 'S') &
                         (df['CSL 331'] == 'S') &
                         (df['CSL 333'] == 'S')]

print("\nStudents who have passed all subjects:")
print(passed_all_subjects[['REGISTER NO', 'NAME']])
