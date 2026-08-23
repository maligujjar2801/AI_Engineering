from abc import ABC , abstractmethod

class Notification(ABC) :
    def send(message) :
        pass

class Email(Notification):
    def send(message):
        print(f"{message} sent through Email.")

class SMS(Notification):
    def send(message):
        print(f"{message} sent through SMS.")

class Push(Notification):
    def send(message):
        print(f"{message} sent through Push.")

routes = [Email(), SMS() ,Push()]

for route in routes :
    route.send("Assalamualaikum")