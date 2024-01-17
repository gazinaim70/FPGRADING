import csv

# Function to display student information
def display_student_info(student_id, students_data):
    student_info = students_data.get(student_id)
    if student_info:
        name, *grades = student_info
        output = f"Name: {name}\n"
        output += "Subjects Grade:\n"
        # Assuming 'subjects' is a list of subject names
        for subject, grade in zip(subjects, grades):
            output += f"{subject}: {grade}\n"
        # Check for any grade less than 65
        if any(int(grade) < 65 for grade in grades):
            output += "Final Result: FAIL"
        else:
            output += "Final Result: PASS"
        return output
    else:
        return "Student ID not found."

# Function to read CSV data into a dictionary
def read_csv_data(filepath):
    students_data = {}
    with open(filepath, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            student_id = int(row['Student ID'])
            # Assuming grades are stored as integers in the CSV
            students_data[student_id] = [row['Name'], row['Math'], row['Science'], row['History']]
    return students_data

# Path to the CSV file
csv_file_path = r'C:\Users\Onu´s gadget\Desktop\fpgradingsystem\students_grades.csv'
students_data = read_csv_data(csv_file_path)

# Assuming the subjects are in the order: Math, Science, History
subjects = ["Math", "Science", "History"]

# Function to get a valid student ID input from the user
def get_valid_student_id():
    while True:
        try:
            student_id_input = int(input("Enter student ID (between 1000 and 1004): "))
            if 1000 <= student_id_input <= 1004:
                return student_id_input
            else:
                print("Forgot your student ID? Here's the ID list: 1000/1001/1002/1003/1004")
        except ValueError:
            print("Forgot your student ID? Here's the ID list: 1000/1001/1002/1003/1004")

# Get a valid student ID from the user
student_id_input = get_valid_student_id()

# Display the information for the input student number
print(display_student_info(student_id_input, students_data))

input("Press any key to exit")
