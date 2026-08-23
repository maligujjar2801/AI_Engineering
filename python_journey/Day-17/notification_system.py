from abc import ABC , abstractmethod

class Notification(ABC) :
    def send(self,message) :
        pass

class Email(Notification):
    def send(self,message):
        print(f"{message} sent through Email.")

class SMS(Notification):
    def send(self,message):
        print(f"{message} sent through SMS.")

class Push(Notification):
    def send(self,message):
        print(f"{message} sent through Push.")

routes = [Email(), SMS() ,Push()]

for route in routes :
    route.send("Assalamualaikum")