# March 10, 2025

class TestClass():
    def __init__(self, name, age, location):
        self.name = name
        self.age = age
        self.__location = location # 2 underscore = private variable 
    def DisplayAge(self):
        print(f'{self.name} age is {self.age}')

class callerClass():
    def __init__(self, testClass : TestClass):
        self.testClass = testClass

    def GetName(self):
        print(f'The person name is {self.testClass.name}')
        print(f'The person lives at {self.testClass.age}')
    
    def GetPersonDetails(self):
        self.testClass.DisplayAge()

person = TestClass('Bob', 15, 'Caloocan')

caller = callerClass(person)

print(person.name)
caller.GetName()
caller.GetPersonDetails()


class Animal():
    def __init__(self, name, age, country, weight):
        self.name = name
        self.age = age
        self.country = country
        self.weight = weight

    def GetDetails(self):
        print(f'Animal name: {self.name}\n Animal age: {self.age}\n Animal Country: {self.country}')

class Action():
    def move(self):
        print(f'this animal is moving')

class Panda(Animal): # this is an example of inheritance
    pass        # to get the same syntax as the Animal() class

class Bird(Animal, Action): # two inheritance
    pass        

class Dog(Animal, Action): # a child inheritance
    pass        

# panda = Panda('xi jin ping', 18, 'China 2nd', 48)
# bird = Bird('Eagle', 3, 'USA', 20)
# dog = Dog('Sarah Duterte', 16, 'Philippines', 18)

# Alternative version
animals = [Panda('xi jin ping', 18, 'China 2nd', 48),
           Bird('Eagle', 3, 'USA', 20), 
           Dog('Sarah Duterte', 16, 'Philippines', 18)]

for animals in animals:
    animals.GetDetails()
    
class BullDog(Dog): # comes from a Dog() which is a child inheritance but making it a mother 
    pass

bulldog = BullDog('aspin', 10, 'USA', 35)
bulldog.GetDetails()
bulldog.move()

