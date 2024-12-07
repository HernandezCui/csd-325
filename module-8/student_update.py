import json

# Function to print the student list in the specified format
def print_student_list(students):
    for student in students:
        print(f"{student['F_Name']} , {student['L_Name']} : ID = {student['Student_ID']} , Email = {student['Email']}")

# Load the student data from the JSON file
def load_students(filename):
    with open(filename, 'r') as file:
        students = json.load(file)
    return students

# Write the updated student data back to the JSON file
def save_students(filename, students):
    with open(filename, 'w') as file:
        json.dump(students, file, indent=4)

def main():
    filename = 'student.json' 
    
    # Load the original student list
    students = load_students(filename)
    
    # Output original student list
    print("Original Student List:")
    print_student_list(students)
    
    # Append your details (fictional student)
    new_student = {
        'F_Name': 'John',
        'L_Name': 'Doe',
        'Student_ID': 99999,  
        'Email': 'johndoe@example.com'  
    }
    students.append(new_student)
    
    # Output updated student list
    print("\nUpdated Student List:")
    print_student_list(students)
    
    # Save the updated list back to the JSON file
    save_students(filename, students)
    
    print("\nStudent list has been updated in the JSON file.")
    
if __name__ == '__main__':
    main()