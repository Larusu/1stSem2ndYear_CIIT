# continuation of exampleFile
from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def Go(self):
        pass

    @abstractmethod
    def Stop(self):
        pass

class Car(Vehicle):
    def Go(self):
        print(f'Car move forward because of green light')

    def Stop(self):
        print(f'Car move forward because of red light')

class Jeep(Vehicle):
    def Go(self):
        print("Jeep move forward")

    def Stop(self):
        pass # without the 'pass' it would become error

car = Car()
car.Go()
car.Stop()




# Polymorphism - can change 

class Shape:
    @abstractmethod
    def Area(self):
        pass

class Circle(Shape):
    def __init__(self, radius : float, type):
        self.radius = radius
        self.type = type

    def Area(self): # pwedeng baguhin ang value ni Area
        return 3.14 * self.radius * 2
    
class Square(Shape):
    def __init__(self, sides : float, height : float, type):
        self.sides = sides
        self.height = height
        self.type = type

    def Area(self):
        return self.sides * self.height * 2
    
shapes = [Circle(6, "Circle"), Square(5, 8, "Square")]

for shape in shapes:
    print(f'{shape.type} Area  is: {shape.Area()}')

# ducktyping