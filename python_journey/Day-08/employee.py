class Employee:
    company = "OpenAI"
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
employee = Employee("Ali", 70000)
print(f"Employee: {employee.name}")
print(f"Company: {employee.company}")