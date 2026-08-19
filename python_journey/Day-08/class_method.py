class Employee:
    company = "OpenAI"
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    @classmethod
    def change_company(cls, new_company):
        cls.company = new_company
employee = Employee("Ali", 70000)
Employee.change_company("Google")
print(f"Employee: {employee.name}")
print(f"Company: {employee.company}")
