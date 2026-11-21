
class Employee:

    def __init__(self, name, employee_id, salary, department):
        self.name = name
        self.employee_id = employee_id
        self.salary = salary
        self.department = department

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Employee ID: {self.employee_id}")
        print(f"Salary: {self.salary}")
        print(f"Department: {self.department}")

    def calculate_annual_salary(self):
        annual_salary = self.salary * 12
        print(f"Annual Salary: {annual_salary}")


employee1 = Employee("Ali", "101", 50000, "IT")
employee2 = Employee("Sara", "102", 60000, "Finance")
employee3 = Employee("Aman", "103", 120000, "HR")

for employee in [employee1, employee2, employee3]:
    employee.display_info()
    employee.calculate_annual_salary()
    print()
