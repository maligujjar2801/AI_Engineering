class Employee :
    def __init__(self, salary):
        self._salary = salary
    def get_salary(self):
        return self._salary
employee = Employee(50000)
print(employee.get_salary())