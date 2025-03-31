# Method
# Instance, Static, Class, Dunder

# Instance Method: used in Objects, requires 'self'
# Static Method: Can be called without creating an instance (no 'self' required) 

class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def get_info(self): # Instance method Implementation
        return f"{self.name} = {self.position}"
    
    @staticmethod       # Static MEthod Implementation
    def is_valid_position(position): 
        """Checks if the given position is in the list of valid positions.""" 
        valid_position = ["Manager", "Cook", "Cashier", "Janitor", "Kuya Guard"]
        return position in valid_position # Returns True if position exists in the list
    
    # Key difference:  
    # - Instance methods use 'self' and require an instance of the class.  
    # - Static methods do not use 'self' and can be called without an instance.

class Boss:
    def __init__(self, name, age, money):
        self.name = name 
        self.age = age
        self.money = money
    
employeeOne = Employee("Spongebob", "Cook")
employeeTwo = Employee("Squidward", "Cashier")
employeeThree = Employee("Mr. Krab", "Manager")
boss = Boss("Mr. Krab", 35, 10000)

print(employeeTwo.get_info())
print(Employee.is_valid_position("Kuya Guard")) # returns true since Kuya Guard is a position in the list