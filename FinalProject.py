# Required Implementation:
#       OOP
#           Encapsulation
#           Inheritance
#           Polymorphism (use either Inheritance Implementation or Duck Typing Implementation)
#           Abstraction
#       Methods (use either of the following: Instance, Static, Class)
# Optional Implementation
#       Aggregation
#       Aggregation and Composition
#       Nested Class
#       Dunder Methods


# Determine if School bus is also an instance of the Vehicle class.
class Vehicle:
    def __init__(self, type: str, wheels: int, color: str, model: str, brand: str, fuel: str) -> None:
        self.type = type
        self.wheels = wheels
        self.color = color
        self.model = model
        self.fuel = fuel
        self.brand = brand

    def description(self):
        print(f"Vehicle: {self.wheels}-wheeler {self.type}\nColor: {self.color}\nBrand and model: {self.brand}, {self.model}\n Fuel type: {self.fuel}")

schoolBus = Vehicle('Bus', 4, 'Yellow', 'V8R', 'Volvo', 'Diesel')

# Output
# schoolBus.description()

# print("\nIs schoolBus a vehicle?", isinstance(schoolBus, Vehicle))



# Build a class Employee with multiple constructors that can initialize an employee object in different ways.
class Employee:
    allowed_position = ['Worker', 'Manager', 'Director', 'CEO']

    def __init__(self, id: int, name: str, age: int, salary: float, position: str):
        self.id = id
        self.name = name
        self.age = age
        self.salary = salary

        if position not in Employee.allowed_position:
            raise ValueError("Invalid Position!")
        self.position = position

        if self.position == 'CEO':
            self.salary = 110000
        elif self.position == 'Director':
            self.salary = 70000
        elif self.position == 'Manager':
            self.salary = 40000
        else: 
            self.salary = 25000

    def get_salary(self):
        print(f'Employee {self.name}\'s salary is {self.salary}')

    def description(self):
        print(f"ID: {self.id}, Name: {self.name}, Age{self.age}, Salary: {self.salary}, Position: {self.position}")

    def in_5_years(self):
        if self.position == 'CEO':
            future_salary = self.salary * 2.5 * 5 
        elif self.position == 'Director':
            future_salary = self.salary * 2.1 * 5
        elif self.position == 'Manager':
            future_salary = self.salary * 1.6 * 5
        else:
            future_salary = self.salary * 1.2 * 5

        print(f'5 years from now, Employee {self.name}\' salary would be {round(future_salary)}')

employee1 = Employee(1, 'John Doe', 25, 26000, 'Worker')
employee2 = Employee(2, 'Jane Smith', 38, 80000, 'Director')
employee3 = Employee(3, 'Garrett Lopez', 26, 46000, 'Manager')
employee4 = Employee(4, 'Henry Sy', 59, 150000, 'CEO')

employee = [employee1, employee2, employee3, employee4]

# Output
# for emp in employee:
    #  emp.get_salary()
    #  emp.description()
    #  emp.in_5_years()




# Build a two class call SchoolOne and SchoolTwo that display there list of students average grades and GPA.
class Grades:
    def __init__(self, no_semester: int, subject: list, grades: list):
        self.no_semester = no_semester
        self.subject = subject
        self.grades = grades
        self.gpa = self.calculate_grade()
    
    def calculate_grade(self):
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades)

class SchoolOne(Grades):
    def __init__(self, name, age, no_semester, subject, grades):
        super().__init__(no_semester, subject, grades)
        self.name = name
        self.age = age
    
        if self.no_semester == 1:
            self.sem = '1st'
        elif self.no_semester == 2:
            self.sem = '2nd'
        elif self.no_semester == 3:
            self.sem = '3rd'
        else:
            self.sem = '4th'
    
    def __str__(self) -> str:
        return f"School One's grade of students"

    def display_student(self):
        print(f'Student: {self.name}, Age: {self.age}, {self.sem} Semester')
        for subject, grade in zip(self.subject, self.grades):
            print(f'Subject: {subject}, Grade: {grade}')
        print(f'GPA: {round(self.gpa, 2)}\n')

class SchoolTwo(SchoolOne):
    def __str__(self):
        return f"School Two's grade of students"
    
    def display_student(self):
        return super().display_student()
    
student1 = SchoolOne('John Doe', 18, 3, ['Math', 'Science', 'AP'], [91, 92, 95])
student2 = SchoolOne('Will Smith', 19, 2, ['Science', 'Filipino', 'English'], [98, 92, 90])
student3 = SchoolOne('Jane Smith', 17, 1, ['TLE', 'Math', 'Programming'], [99, 91, 89])
schoolOne_Students= [student1, student2, student3]

student4 = SchoolTwo('Garrett Lopez', 15, 2, ['Science', 'Filipino', 'English'], [88, 92, 93])
student5 = SchoolTwo('Blake Giles', 18, 4, ['Math', 'Science', 'AP'], [97, 97, 93])
student6 = SchoolTwo('Kayson Cross', 20, 4, ['TLE', 'Math', 'Programming'], [91, 98, 98])
schoolTwo_Students = [student4, student5, student6]
    

# Output
# for schoolone in schoolOne_Students:
#     schoolone.display_student()

# for schooltwo in schoolTwo_Students:
#     schooltwo.display_student()



# Operator Overloading Create a Vector class that supports addition using the + operator, allowing you to add two vectors.
class Vector:
    def __init__(self, x = 0, y = 0) -> None:
        self.x = x
        self.y = y
    
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    
    def __str__(self) -> str:
        return f"Vector({self.x}, {self.y})"

vector1 = Vector(23, 25)
vector2 = Vector(27, 32)
vector3 = Vector(14, 15)

# Output
# print(vector1)
# print(vector2)
# print(vector3)


# Composition Over Inheritance: Create a Book class with a Author class included within it, demonstrating composition over inheritance.
class Author:
    def __init__(self, name, age, email) -> None:
        self.name = name
        self.age = age
        self.email = email
    
    def __str__(self):
        return f"{self.name}, {self.age} years old"
    
    def get_email(self):
        return f"{self.email}"
    
    class Book:
        def __init__(self, title, author):
            self.title = title
            self.author = author

        def get_details(self):
            print(f'Book Title{self.title} by {self.author}\n Contact the author using this email: {self.author.get_email}')


author1 = Author('Erica Jong', 83, 'erica_jong@gmail.com')
author2 = Author('Donald J. Sobol', 87, 'donald_sobol@gmail.com')

book1 = Author.Book('Fear of Flying', author1)
book2 = Author.Book('Loves Comes First', author1)
book3 = Author.Book('Encyclopedia Brown, Boy Detective', author2)
book4 = Author.Book('Encyclopedia Brown and his Best Cases Ever', author2)

books = [book1, book2, book3, book4]

# # Output
for book in books:
    book.get_details()