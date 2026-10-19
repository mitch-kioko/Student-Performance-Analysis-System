import csv


class Student:
    def __init__(self, student_id, first_name, last_name, programme, marks):
        self.student_id = student_id
        self.first_name = first_name
        self.last_name = last_name
        self.programme = programme
        self.marks = marks

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
            return 0
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

    def display_student_info(self):
        pass

class AIUStudent(Student):
    def display_student_info(self):
        print(f"Student ID: {self.student_id}")
        print(f"Name: {self.first_name} {self.last_name}")
        print(f"Programme: {self.programme}")
        print(f"Marks: {self.marks}")
        print(f"Average: {self.calculate_average()}")
        print(f"Grade: {self.determine_grade()}")


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
        highest_avg_student = max(self.students, key=lambda student: student.calculate_average())
        return highest_avg_student

    def lowest_average(self):
        lowest_avg_student = min(self.students, key=lambda student: student.calculate_average())
        return lowest_avg_student

    def average_marks(self):
        if len(self.students) == 0:
            return 0

        total_marks = sum(student.calculate_average() for student in self.students)
        return total_marks / len(self.students)

student1 = AIUStudent("25/222", "Sandra", "Mutegi", "BBA", marks=[90, 79, 100, 82, 94])
student2 = AIUStudent("25/224", "Carlos", "Ndunda", "BAFM", marks=[88, 80, 97, 86, 96])
student3 = AIUStudent("25/226", "Paul", "Omboga", "DBIT", marks=[86, 81, 94, 96, 98])
student4 = AIUStudent("25/228", "Ruth", "Mwikali", "BBA", marks=[84, 82, 91, 94, 100])
student5 = AIUStudent("25/230", "Oscar", "Juma", "BAI", marks=[83, 83, 90, 98, 100])
student6 = AIUStudent("25/232", "Yusuf", "Hakim", "BAI", marks=[82, 84, 89, 83, 91])
student7 = AIUStudent("25/234", "Sylvester", "John", "DAI", marks=[81, 85, 88, 90, 95])
student8 = AIUStudent("25/236", "Abdullahi", "Mohamud", "DAI", marks=[80, 86, 87, 92, 100])
student9 = AIUStudent("25/238", "Mohamed", "Adan", "DBIT", marks=[79, 87, 86, 97, 99])
student10 = AIUStudent("25/240", "Shilah", "Wanjiru", "BAFM", marks=[78, 88, 89, 99, 97])

students = [student1, student2, student3, student4, student5, student6, student7, student8, student9, student10]
analyzer = PerformanceAnalyzer(students)

highest_avg_student = analyzer.highest_average()
lowest_avg_student = analyzer.lowest_average()

print("Highest Average:", highest_avg_student.first_name, highest_avg_student.calculate_average())

print("Lowest Average:", lowest_avg_student.first_name, lowest_avg_student.calculate_average())

print("Overall Average Marks:", analyzer.average_marks())

class scholarshipEligibility(AIUStudent):
    def __init__(self, student_id, first_name, last_name, programme, marks):
        super().__init__(
            student_id,
            first_name,
            last_name,
            programme,
            marks
        )

    def is_eligible_for_scholarship(self):
        average = self.calculate_average()
        return average >= 88

    def display_student_info(self):
        super().display_student_info()
        if self.is_eligible_for_scholarship():
            print("Eligible for Scholarship: Yes")
        else:
            print("Eligible for Scholarship: No")

    def display_scholarship_eligible_students(self, students):
        print("Scholarship Eligible Students:")
        for student in students:
            if student.is_eligible_for_scholarship():
                print(f"{student.first_name} {student.last_name} - Average: {student.calculate_average()}")

student1 = AIUStudent("25/222", "Sandra", "Mutegi", "BBA", marks=[90, 79, 100, 82, 94])
student2 = scholarshipEligibility("25/224", "Carlos", "Ndunda", "BAFM", marks=[88, 80, 97, 86, 96])
students = [student1, student2]

for student in students:
    student.display_student_info()
    print()

    def calculate_average(self):
        if len(self.marks) == 0:
            raise ValueError("No marks available to calculate average.")
        
        for mark in self.marks:
            if not isinstance(mark, (int, float)):
                raise ValueError("All marks must be numeric values.")

        for mark in self.marks:
            if mark < 0 or mark > 100:
                raise ValueError("Marks must be between 0 and 100.")

        return sum(self.marks) / len(self.marks)

    print("Average of two marks:", student1.calculate_average())
    print("Average of three marks:", student2.calculate_average())

    def load_students(filename):
        students = []
        with open(filename, "r", newline="", encoding="utf-8-sig") as csvfile:
            reader = csv.reader(csvfile)
            next(reader)  
            for row in reader:
                student = AIUStudent(
                    student_id=row[0],
                    first_name=row[1],
                    last_name=row[2],
                    programme=row[3],
                    marks=[int(mark) for mark in row[4].split(',')]
                )
                students.append(student)
        return students

    def generate_report_card(self):
        report_card = f"Report Card for {self.first_name} {self.last_name}\n"
        report_card += f"Programme: {self.programme}\n"
        report_card += f"Marks: {self.marks}\n"
        report_card += f"Average: {self.calculate_average()}\n"
        report_card += f"Grade: {self.determine_grade()}\n"
        report_card += f"Scholarship Eligibility: {'Yes' if self.is_eligible_for_scholarship() else 'No'}\n"
        return report_card

    print("Highest Average:", highest_avg_student.get_first_name(), highest_avg_student.get_last_name(), highest_avg_student.calculate_average())
    print("Lowest Average:", lowest_avg_student.get_first_name(), lowest_avg_student.get_last_name(), lowest_avg_student.calculate_average())
    print("Overall Average Marks:", analyzer.average_marks())

print("Loaded Students from CSV:")
for student in students:
    student.display_student_info()
    print()

