class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display(self):
        print("Employee Name:", self.name)
        print("Employee Salary:", self.salary)
        
emp1 = Employee("Rahul", 25000)

emp1.display()