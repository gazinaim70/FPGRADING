import csv

# Class definition
class Student:
    def __init__(self, student_id, name, grades):
        self.student_id = student_id
        self.name = name
        self.grades = grades

    def display_info(self, grade_margins):
        output = f"Name: {self.name}\nSubjects Grade:\n"
        for subject, grade in zip(subjects, self.grades):
            letter_grade = get_letter_grade(int(grade), grade_margins)
            output += f"{subject}: {grade} ({letter_grade})\n"
        if any(int(grade) < 65 for grade in self.grades):
            output += "Final Result: FAIL"
        else:
            output += "Final Result: PASS"
        return output

# Function definitions
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

def read_grade_margins(filepath):
    grade_margins = []
    with open(filepath, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            min_score = int(row['Min_Score'])
            max_score = int(row['Max_Score'])
            grade = row['Grade']
            grade_margins.append((min_score, max_score, grade))
    return grade_margins

def get_letter_grade(numeric_grade, grade_margins):
    for min_score, max_score, grade in grade_margins:
        if min_score <= numeric_grade <= max_score:
            return grade
    return 'Unknown Grade'

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

# Main execution
if __name__ == "__main__":
    # Path to the CSV files
    csv_file_path = 'students_grades.csv'
    grade_margins_file_path = 'grade_margins.csv'
    
    # Read data from CSV files
    students_data = read_csv_data(csv_file_path)
    grade_margins = read_grade_margins(grade_margins_file_path)

    # Assuming the subjects are in the order: Math, Science, History
    subjects = ["Math", "Science", "History"]

    # Get a valid student ID from the user
    student_id_input = get_valid_student_id()

    # Display the information for the input student number
    print(students_data[student_id_input].display_info(grade_margins))

    # Wait for user input to exit the program
    while True:
        user_input = input("Type 'exit' to finish: ")
        if user_input.lower() == 'exit':
            break
