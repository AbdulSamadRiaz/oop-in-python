class Person:

    def __init__(self,name,age):
        self.name = name
        self.age = age


class Student(Person):

    def __init__(self,name,age,roll_no,semester):
        super().__init__(name,age)
        self.roll_no = roll_no
        self.semester = semester

    def display_info(self):
        print("=========STUDENT INFORMATION==========")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Roll no: {self.roll_no}")
        print(f"Semester: {self.semester}")


class Teacher(Person):

    def __init__(self,name,age,employee_id,subject):
         super().__init__(name,age)
         self.employee_id = employee_id
         self.subject = subject


    def display_info(self):
        print("=========TEACHER INFORMATION==========")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Employee id: {self.employee_id}")
        print(f"Subject: {self.subject}")


student1 = Student("Samad",21,"S101", "3rd")
teacher1 = Teacher("Ali",34,"T101", "Programming")

student1.display_info()
print("-----------------------------")
teacher1.display_info()

