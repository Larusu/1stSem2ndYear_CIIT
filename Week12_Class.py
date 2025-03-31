# Class Method:
# inaaccess lahat ng independent variable sa iisang class?

class Student:
    # Plan: Keep track of total students and cumulative GPA
    count = 0  # Class variable to count total students
    total_GPA = 0  # Class variable to sum all GPAs

    def __init__(self, name:str, GPA:float):
        self.name = name # Instance variable for student name
        self.GPA = GPA  # Instance variable for student GPA
        Student.count += 1  # Increment student count on each instance
        Student.total_GPA += GPA  # Add GPA to total GPA
    
    def get_student_info(self): # Instance Method
        return f"{self.name} {self.GPA}"
    
    @classmethod # Class Method Implementation
    def get_count(cls): # uses a CLS to get all the info in class or in this case the independent variable of "count"
    # Returns the total number of students created.
        return f"Total # of Student: {cls.count}"
    
    @classmethod
    # Calculates and returns the average GPA of all students.
    def get_average_gpa(cls):
        return f"{cls.total_GPA / cls.count: 0.2f} GPA"
    
students = [Student("Mike", 3.5), Student("Barbie", 3.0), Student("Lars", 2.9)]

print(Student.get_count())       # Output: Total # of Students: 3
print(Student.get_average_gpa()) # Output: Average GPA: 3.13

# Key differences:
# - Instance methods use 'self' and work with specific objects.
# - Static methods (@staticmethod) do not access class or instance variables.
# - Class methods (@classmethod) use 'cls' and can access class variables.