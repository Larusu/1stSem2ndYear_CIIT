'''Duck Typing'''
# Duck typing is a type system where an object is considered compatible with a given type 
# if it has all the methods and attributes that the type requires. This type system supports 
# the ability to use objects of independent and decoupled classes in a specific context as 
# long as they adhere to some common interface.

class Animal:
    alive = True

class Dog(Animal):
    def Speak(self):
        print("Woof!")

class Cat(Animal):
    def Speak(self):
        print("Meow!")

class Car:
    def Horn(self):
        print("Beep beep!")

class Jeep:
    alive = False

    def Speak(self):
        print("I'm a talking jeep")

animals = [Dog(), Cat(), Car()]
animals2 = [Dog(), Cat(), Jeep()]

# for animal in animals:
#     animal.Speak() # Error!!! because Car function is Horn() not Speak()


# From ChatGPT:
# Duck typing is a concept where an object's usability depends on its methods and attributes rather than its specific class.
# In this example, the `Speak()` method is defined in Dog, Cat, and Jeep classes.
# Even though Jeep is not a subclass of Animal, it still works in the loop because it has a `Speak()` method.
# The `alive` attribute is also accessed regardless of the object's actual class.
# This flexibility is a key feature of dynamic typing in Python.
for animal in animals2:
    animal.Speak()
    print(animal.alive) 

print()

'''Aggregation'''
# ChatGPT
# Aggregation is a relationship where one class contains objects of another class but does not own them.
# In this case, the Library class contains Book objects, but books can exist independently of the library.

class Library:
    def __init__(self, name):
        self.name = name
        self.books = [] # initializes an empty list to store book objects.
                        # this list acts as a container for books that will be added to the library.

    def add_book(self, book):
        self.books.append(book) # append() method is used to add a new book objects to the 'books' list
                                # It modifies the list in place by inserting the given book at the end of the list
    
    def list_books(self):
        return [f"{book.book_title} by {book.book_author}" for book in self.books]

class Book:
    def __init__(self, book_title, book_author):
        self.book_title = book_title
        self.book_author = book_author

library = Library("CIIT Library")

book1 = Book("Python Programming for Beginners", "Mark Tahimik lang")
book2 = Book("Java Programming for Beginners", "John Abotnatin")

print(library.name)
for book in library.list_books():
    print(book)

print()

'''Aggregation and Composition'''
# ChatGPT
# Composition: A strong relationship where the contained objects (Engine and Wheel) cannot exist without the parent object (Car).
# Aggregation: A weaker relationship where an object can exist independently from the main object.

class Engine:
    def __init__(self, horse_power):
        self.horse_power = horse_power

class Wheel:
    def __init__(self, size):
        self.size = size

class Car1:
    def __init__(self, manufacturer, model, horse_power, wheel_size):
        self.manufacturer = manufacturer # stores the car manufacturer
        self.model = model # Stores the car model

        # Composition: The engine is an essential part of the Car
        # A car cannot function without an engine, so it's created inside the Car Class.
        self.engine = Engine(horse_power)

        # Composition: A Car has four Wheels, which are created when the Car is instantiated.
        # This ensures that the Car owns the wheels.
        self.wheel = [Wheel(wheel_size) for _ in range(4)]

    def display_car_details(self):
        return f"{self.manufacturer}, {self.model}, {self.engine.horse_power}, {self.wheel[0].size}"
    
car = Car1("Ford", "Mustang Shelby GT500", 500, 4)

print(car.display_car_details())

print("\n")

'''Nested Class'''
# A nested class is a class defined inside another class.
# It is useful when the inner class is logically related to the outer class and does not need to exist independently.

class LethalCompany:
    class Employee: # Nested Class / sub class
        def __init__(self, name, position):
            self.name = name # Stores the employee name
            self.position = position # Store the employee position

        def get_details(self):
            return f"Name: {self.name} \n Position: {self.position}"

    def __init__(self, name):
        self.name = name # Stores the company name
        self.employees = [] # Initializes an empty list to store Employee objects

    def add_employee(self, employee_name, employee_position):
        # Creates a new Employee object using the nested class.
        # Since Employee is nested, we access it using `self.Employee()`.
        new_employee = self.Employee(employee_name, employee_position)
        self.employees.append(new_employee) # adds the employee to list

    def list_employees(self):
        return [employee.get_details() for employee in self.employees]

# Creating a LethalCompany object named "Krusty Krab"
company = LethalCompany("Krasty Krab")

# Adding employees to the company
company.add_employee("Spongebob Squarepants", "Cook")
company.add_employee("Squidward","Cashier")
company.add_employee("Mr. Krabs","Manager")

for employee in company.list_employees():
    print(employee)

# This example demonstrates a nested class in Python.
# The `Employee` class is defined inside the `REPO` class because employees are logically associated with a company.
class REPO:
    class Employee:
        def __init__(self, name, position):
            self.name = name
            self.position = position

        def display_details(self):
            return f"Name: {self.name}, Position: {self.position}"
    
    def __init__(self, name, employee_name, employee_position):
        self.name = name

        # Creating an instance of the nested Employee class.
        # Since `Employee` is inside `REPO`, we must call it as `self.Employee()`.
        self.employee = self.Employee(employee_name, employee_position)

companyTwo = REPO("Chum Bucket", "Sheldon", "Manager")

print(companyTwo.name)
print(companyTwo.employee.display_details())

# ...

