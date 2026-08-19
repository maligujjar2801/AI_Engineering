class Employee :
    def work(self):
        print("Does his work.")

class Manager(Employee) :
    def work(self) :
        print("Manages all the tasks. ")

class Designer(Employee):
    def work(self) :
        print("Designs the products. ")

class Developer(Employee):
    def work(self):
        print("Developes the software. ")

manager = Manager()
dev = Developer()
designer = Designer()
dev.work()
designer.work()
manager.work()