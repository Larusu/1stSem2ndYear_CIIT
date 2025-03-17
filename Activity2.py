# Activity 2 - Python OOP

# Exercise 1 
class Calculator():
    def __init__(self, num1 : int, num2 : int):
        self.num1 = num1
        self.num2 = num2

    def addNum(self):
        return self.num1 + self.num2
    
    def subtNum(self):
        return self.num1 - self.num2

# example
calc = Calculator(32, 10)
print(calc.addNum())
print(calc.subtNum())
print()

# Exercise 2
class Person():
    def __init__(self, name : str, country : str, age : int, birthdate : str):
        self.name = name
        self.country = country
        self.age = age
        self.birthdate = birthdate

    def knowCharacterAge(self):
        print(f'The person {self.name} is {self.age} years old')

# Example 
person1 = Person('Lars', 'Philippines', 18, 'May 19')
person1.knowCharacterAge()
print()

# Exercise 3

class Vehicle():
    def __init__(self, model: str, brand: str, color: str, speed: float):
        self.model = model
        self.brand = brand
        self.color = color
        self.speed = speed

    # Appending "km/hr" in speed
    @property # define a method that acts like an attribute
    def speed(self):
        return f"{self._speed} km/hr"
    
    @speed.setter # allowing to modify the speed attribute
    def speed(self, value: float):
        self._speed = value


    def getCarInfo(self):
        print(f'Car Information\n Model: {self.model}\n Brand: {self.brand}\n Color: {self.color}\n Speed: {self.speed}')

class Bus(Vehicle):
    pass

# Example
bussing = Bus('NV350', 'Nissan', 'White', 70.5)
bussing.getCarInfo()
