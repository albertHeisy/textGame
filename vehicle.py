class Vehicle:
    def __init__(self):
        raise NotImplementedError('You must see a subclass.')

class Motorcycle(Vehicle):
    def __init__(self):
        self.wheels = 2

class Car(Vehicle):
    def __init__(self):
        self.wheels = 4

def main():
    yamaha = Motorcycle()
    toyota = Car()
    honda = Vehicle()
    print(yamaha.wheels,toyota.wheels)

main()
    
