# Student Result Management System

class StudentResultManagementSystem:
    def __init__(self, name, matric_number, score):
        self.name = name
        self.matric_number = matric_number
        self.score = score

    def calculate_grade(self):
        if self.score >= 70:
            return "A"
        elif self.score >= 60:
            return "B"
        elif self.score >= 50:
            return "C"
        elif self.score >= 45:
            return "D"
        else:
            return "F"

    def display_result(self):
        grade = self.calculate_grade()
        print("Student Name:", self.name)
        print("Matric Number:", self.matric_number)
        print("Score:", self.score)
        print("Grade:", grade)


# Main program
name = input("Enter student name: ")
matric_number = input("Enter matric number: ")
score = int(input("Enter score: "))

# Create a student object
student = StudentResultManagementSystem(name, matric_number, score)

# Display the result
student.display_result()
