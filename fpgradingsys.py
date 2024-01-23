import csv

# Define the Student class to represent student data
class Student:
    def __init__(self, student_id, name, grades):
        # Initialize the Student object with ID, name, and grades
        self.student_id = student_id
        self.name = name
        self.grades = grades

    def display_info(self, grade_margins):
        # Display student information including name, grades, and letter grades
        output = f"Name: {self.name}\nSubjects Grade:\n"
        for subject, grade in zip(subjects, self.grades):
            letter_grade = get_letter_grade(int(grade), grade_margins)
            output += f"{subject}: {grade} ({letter_grade})\n"
        if any(int(grade) < 65 for grade in self.grades):
            output += "Final Result: FAIL"
        else:
            output += "Final Result: PASS"
        return output

# Function to read student data from a CSV file
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

# Function to read grading margins from a CSV file
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

# Function to convert numeric grade to letter grade based on margins
def get_letter_grade(numeric_grade, grade_margins):
    for min_score, max_score, grade in grade_margins:
        if min_score <= numeric_grade <= max_score:
            return grade
    return 'Unknown Grade'

# Function to calculate progress between two sets of grades
def calculate_progress(grades_sem1, grades_sem2):
    progress = {}
    for subject in grades_sem1.keys():
        grade1, grade2 = int(grades_sem1[subject]), int(grades_sem2[subject])
        change = grade2 - grade1
        percent_change = (change / grade1) * 100 if grade1 != 0 else float('inf')
        progress[subject] = percent_change
    return progress

# Function to get a valid student ID from user input
def get_valid_student_id():
    while True:
        try:
            student_id_input = int(input("Enter student ID: "))
            if 1000 <= student_id_input <= 1004:
                return student_id_input
            else:
                print("Forgot your student ID? It should be 1000/1001/1002/1003/1004")
        except ValueError:
            print("Invalid input. Please enter a number.")

# Main execution block
if __name__ == "__main__":
    # File paths for CSV files
    csv_file_path_sem1 = 'students_grades.csv'
    csv_file_path_sem2 = 'student_grades_sem2.csv'
    grade_margins_file_path = 'grade_margins.csv'
    
    # Read data from CSV files
    students_data_sem1 = read_csv_data(csv_file_path_sem1)
    students_data_sem2 = read_csv_data(csv_file_path_sem2)
    grade_margins = read_grade_margins(grade_margins_file_path)

    # Subjects in the order they appear in the CSV files
    subjects = ["Math", "Science", "History"]

    # Get valid student ID from user
    student_id_input = get_valid_student_id()

    # Retrieve student information for each semester
    student_sem1 = students_data_sem1.get(student_id_input)
    student_sem2 = students_data_sem2.get(student_id_input)

    # Display student grades and progress if data exists
    if student_sem1 and student_sem2:
        print("Semester 1 Grades:")
        print(student_sem1.display_info(grade_margins))

        print("\nSemester 2 Grades:")
        print(student_sem2.display_info(grade_margins))

        print("\nProgress from Semester 1 to Semester 2:")
        progress = calculate_progress(dict(zip(subjects, student_sem1.grades)), 
                                      dict(zip(subjects, student_sem2.grades)))
        for subject, percent_change in progress.items():
            print(f"{subject} Progress: {percent_change:+.2f}%")
    else:
        print("Student data not found for the given ID.")

    # Exit mechanism
    while True:
        user_input = input("Type 'exit' to finish: ")
        if user_input.lower() == 'exit':
            break
 
                

    
        


