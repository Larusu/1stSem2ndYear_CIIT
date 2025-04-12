number : str = '213' #

print(int(number) + 1)


class Car():
    def __init__(self, brand:str, color:str, horsePower: float): #initialize
        self.brand = brand
        self.color = color
        self.horsePower = horsePower
            
    def get_info(self): # Always use self
        print(f'{self.brand} has a color of {self.color} with a horse power of {self.horsePower}hp')
    
    def __str__(self):  #nNo need to specify when printing
        return f'{self.brand}, {self.color}, {self.horsePower}'
				
# Creating Objects
BMW : Car = Car('BMW', 'White', 100)
Toyota : Car = Car('Toyota', 'Red', 130)

print(BMW.brand)

BMW.get_info() # Calling method

print(BMW) # No need to specify since it is  already specified by __str__