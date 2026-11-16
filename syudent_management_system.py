
class student:

    def __init__(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks

    def display_info(self):
        print(f"Student name: {self.name}")
        print(f"Student roll no: {self.roll_no}")
        print(f"Student marks: {self.marks}")

    def calculate_percentage(self):
        self.total_marks = 500
        self.percentage = (self.marks / self.total_marks) * 100
        print(f"Percentage: {self.percentage}%")

    def check_grade(self):

        if self.percentage >= 90:
            print("Grade: A+")

        elif self.percentage >= 80:
            print("Grade: A")

        elif self.percentage >= 70:
            print("Grade: B")

        elif self.percentage >= 60:
            print("Grade: C")

        elif self.percentage >= 50:
            print("Grade: D")

        else:
            print("Grade: Fail")


student1 = student("Abdul Samad Riaz", "BSE-25S-630", 400)

student1.display_info()
student1.calculate_percentage()
student1.check_grade()
