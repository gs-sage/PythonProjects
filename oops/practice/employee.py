class Employee:
    def __init__(self, role, dept, salary):
        self.role = role
        self.dept = dept
        self.salary = salary

    def show_details(self):
        print(f"Role: {self.role}, Department: {self.dept}, Salary: {self.salary}")



emp1 = Employee("Engineer","IT","$90,000")
emp1.show_details()

class Engineer(Employee):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        super().__init__("Engineer", "IT", "$90,000")

    def show_details_engineer(self):
        print(f"Name: {self.name}, Age: {self.age}")


emp2 = Engineer("Gaurav", 30)
emp2.show_details_engineer()
emp2.show_details()

