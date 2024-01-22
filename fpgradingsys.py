import csv

class Student:
    def __init__(self, student_id, name, grades):
        self.student_id = student_id
        self.name = name
        self.grades = grades

    def display_info(self):
        output = f"Name: {self.name}\nSubjects Grade:\n"
        for subject, grade in zip(subjects, self.grades):
            output += f"{subject}: {grade}\n"
        if any(int(grade) < 65 for grade in self.grades):
            output += "Final Result: FAIL"
        else:
            output += "Final Result: PASS"
        return output

def read_csv_data(filepath):
    students_data = {}
    with open(filepath, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            student_id = int(row['Student ID'])
            name = row['Name']
            grades = [row['Math'], row['Science'], row['History']]
            students_data[student_id] = Student(student_id, name, grades)
    return students_data

<<<<<<< Updated upstream
# Path to the CSV file
csv_file_path = r'students_grades.csv'
students_data = read_csv_data(csv_file_path)
=======
def display_student_info(student_id, students_data):
    student = students_data.get(student_id)
    if student:
        return student.display_info()
    else:
        return "Student ID not found."
>>>>>>> Stashed changes

def get_valid_student_id():
    while True:
        try:
            student_id_input = int(input("Enter student ID (between 1000 and 1004): "))
            if 1000 <= student_id_input <= 1004:
                return student_id_input
            else:
                print("Invalid range. Please enter a student ID between 1000 and 1004.")
        except ValueError:
            print("Invalid input. Please enter a number.")
<<<<<<< Updated upstream
=======

# Path to the CSV file
csv_file_path = r'students_grades.csv'
students_data = read_csv_data(csv_file_path)

# Assuming the subjects are in the order: Math, Science, History
subjects = ["Math", "Science", "History"]
>>>>>>> Stashed changes

# Get a valid student ID from the user
student_id_input = get_valid_student_id()

# Display the information for the input student number
print(display_student_info(student_id_input, students_data))

# Wait for user input to exit the program
while True:
    user_input = input("Type 'exit' to finish: ")
    if user_input.lower() == 'exit':
        break
<<<<<<< Updated upstream

            
=======
>>>>>>> Stashed changes
