import csv
import os

class Student:
    def __init__(self, student_id, first_name, last_name, programme, marks):
        self.student_id = student_id
        self.first_name = first_name
        self.last_name = last_name
        self.programme = programme
        self.marks = marks

#Accessing student details        

    def get_student_id(self):
        return self.student_id

    def get_first_name(self):
        return self.first_name

    def get_last_name(self):
        return self.last_name

    def get_programme(self):
        return self.programme

    def get_marks(self):
        return self.marks

#Replacing existing values       

    def set_first_name(self, first_name):
        self.first_name = first_name

    def set_last_name(self, last_name):
        self.last_name = last_name

    def set_programme(self, programme):
        self.programme = programme

    def set_marks(self, marks):
        self.marks = marks

    def calculate_average(self):
        if len(self.marks) == 0:
            raise ValueError("No marks to be calculated")

        for mark in self.marks:
            if isinstance(mark, bool) or not isinstance(mark, (int, float)):
                raise ValueError("All marks must be numeric values.")
          
            if mark < 0 or mark > 100:
                raise ValueError("Marks must be between 0 and 100.")
 
        return sum(self.marks) / len(self.marks)

    def determine_grade(self):
        average = self.calculate_average()
        if average >= 70:
            return 'A'
        elif average >= 60:
            return 'B'
        elif average >= 50:
            return 'C'
        elif average >= 40:
            return 'D'
        else:
            return 'F'

    def is_eligible_for_scholarship(self):
        return self.calculate_average() >= 88

    def display_student_info(self):
        pass

    def generate_report_card(self):
        report_card = f"Report Card for {self.first_name} {self.last_name}\n"
        report_card += f"Programme: {self.programme}\n"
        report_card += f"Marks: {self.marks}\n"
        report_card += f"Average: {self.calculate_average()}\n"
        report_card += f"Grade: {self.determine_grade()}\n"
        report_card += f"Scholarship Eligibility: {'Yes' if self.is_eligible_for_scholarship() else 'No'}\n"
        return report_card


class AIUStudent(Student):
    def display_student_info(self):
        print(f"Student ID: {self.student_id}")
        print(f"Name: {self.first_name} {self.last_name}")
        print(f"Programme: {self.programme}")
        print(f"Marks: {self.marks}")
        print(f"Average: {self.calculate_average()}")
        print(f"Grade: {self.determine_grade()}")

class scholarshipEligibility(AIUStudent):
    def display_student_info(self):
        super().display_student_info()
        if self.is_eligible_for_scholarship():
            print("Eligible for Scholarship: Yes")
        else:
            print("Eligible for Scholarship: No")

    @staticmethod
    def display_scholarship_eligible_students(self, students):
        print("Scholarship Eligible Students:")
        for student in students:
            if student.is_eligible_for_scholarship():
                print(f"{student.first_name} {student.last_name} - Average: {student.calculate_average():.2f}")
student1 = AIUStudent(
    "25/222",
    "Sandra",
    "Mutegi",
    "BBA",
    marks= [90, 79, 100, 82, 94]
)
student1.display_student_info()


class PerformanceAnalyzer:
    def __init__(self, students):
        self.students = students

    def highest_average(self):
        if not self.students:
            raise ValueError("No students to analyse!")
        return max(self.students, key=lambda student: student.calculate_average())

    def lowest_average(self):
        if not self.students:
            raise ValueError("No students to analyse!")
        return min(self.students, key=lambda student: student.calculate_average()) 

    def average_marks(self):
        if len(self.students) == 0:
            return 0
        total_marks = sum(student.calculate_average() for student in self.students)
        return total_marks / len(self.students)

#Load the CSV file
def load_students(filename):
  
    students = []
    with open(filename, "r", newline="", encoding="utf-8-sig") as csvfile:
        rows = list(csv.reader(csvfile))
 
    # Find the header row (skips the title and blank rows)
    header_index = None
    for i, row in enumerate(rows):
        if row and row[0].strip().upper() == "STUDENT ID":
            header_index = i
            break
    if header_index is None:
        raise ValueError("Could not find a header row starting with 'STUDENT ID'.")
 
    header = [cell.strip().upper() for cell in rows[header_index]]
    id_col = header.index("STUDENT ID")
    first_col = header.index("FIRST NAME")
    last_col = header.index("LAST NAME")
    programme_col = header.index("PROGRAMME")
    # Every named column after PROGRAMME is a subject (marks) column
    mark_cols = [i for i, name in enumerate(header) if name and i > programme_col]
 
    for line_no, row in enumerate(rows[header_index + 1:], start=header_index + 2):
        if not any(cell.strip() for cell in row):
            continue  # skip blank rows
        try:
            marks = []
            for i in mark_cols:
                text = row[i].strip()
                marks.append(float(text) if "." in text else int(text))
            student = scholarshipEligibility(
                student_id=row[id_col].strip(),
                first_name=row[first_col].strip(),
                last_name=row[last_col].strip(),
                programme=row[programme_col].strip(),
                marks=marks
            )
            students.append(student)
        except (IndexError, ValueError) as error:
            print(f"Missing line {line_no}: {error}")
    return students
 


def main():
    students = [
        AIUStudent("25/222", "Sandra", "Mutegi", "BBA", marks=[90, 79, 100, 82, 94]),
        AIUStudent("25/224", "Carlos", "Ndunda", "BAFM", marks=[88, 80, 97, 86, 96]),
        AIUStudent("25/226", "Paul", "Omboga", "DBIT", marks=[86, 81, 94, 96, 98]),
        AIUStudent("25/228", "Ruth", "Mwikali", "BBA", marks=[84, 82, 91, 94, 100]),
        AIUStudent("25/230", "Oscar", "Juma", "BAI", marks=[83, 83, 90, 98, 100]),
        AIUStudent("25/232", "Yusuf", "Hakim", "BAI", marks=[82, 84, 89, 83, 91]),
        AIUStudent("25/234", "Sylvester", "John", "DAI", marks=[81, 85, 88, 90, 95]),
        AIUStudent("25/236", "Abdullahi", "Mohamud", "DAI", marks=[80, 86, 87, 92, 100]),
        AIUStudent("25/238", "Mohamed", "Adan", "DBIT", marks=[79, 87, 86, 97, 99]),
        AIUStudent("25/240", "Shilah", "Wanjiru", "BAFM", marks=[78, 88, 89, 99, 97]),
    ]

    analyzer = PerformanceAnalyzer(students)
    highest = analyzer.highest_average()
    lowest = analyzer.lowest_average()
    print("Highest Average:", highest.first_name, highest.last_name, round(highest.calculate_average(), 2))
    print("Lowest Average:", lowest.first_name, lowest.last_name, round(lowest.calculate_average(), 2))
    print("Overall Average Marks:", round(analyzer.average_marks(), 2))
    print()

    csv_file = "studentanalysis.csv"
    if os.path.exists(csv_file):
        print("Loaded Students from CSV:")
        for student in load_students(csv_file):
            student.display_student_info()
            print()
    else:
        print(f"'{csv_file}' not found.")

if __name__ == "__main__":
    main()
