"""
built-in @property decorator which makes usage of getters and setters much easier in Object-Oriented Programming.
"""


# 1. Implementation without getter and setter

# Basic method of setting and getting attributes in Python, involves direct access of class attribute.
class Celsius:
    def __init__(self, temperature=0):
        self.temperature = temperature

    def to_fahrenheit(self):
        return (self.temperature * 1.8) + 32


# Create a new object
human = Celsius()

# Set the temperature
human.temperature = 37

# Get the temperature attribute
print(human.temperature)

# Get the to_fahrenheit method
print(human.to_fahrenheit())


# 2. Use of getter and setter

# Making Getters and Setter methods
class Celsius:
    def __init__(self, temperature=0):
        self.set_temperature(temperature)

    def to_fahrenheit(self):
        return (self.get_temperature() * 1.8) + 32

    # getter method
    def get_temperature(self):
        return self._temperature

    # setter method
    def set_temperature(self, value):
        if value < -273.15:
            raise ValueError("Temperature below -273.15 is not possible.")
        self._temperature = value


# Create a new object, set_temperature() internally called by __init__
human = Celsius(37)

# Get the temperature attribute via a getter
print(human.get_temperature())

# Get the to_fahrenheit method, get_temperature() called by the method itself
print(human.to_fahrenheit())

# new constraint implementation
human.set_temperature(-300)

# Get the to_fahreheit method
print(human.to_fahrenheit())


# 3. After implementation of getter and setter we lost backward compatibility where we could have accessed directly.
# However, the bigger problem with the above update is that all the programs that implemented our previous class have
# to modify their code from obj.temperature to obj.get_temperature() and
# all expressions like obj.temperature = val to obj.set_temperature(val).
#
# This refactoring can cause problems while dealing with hundreds of thousands of lines of codes.
#  All in all, our new update was not backwards compatible. This is where @property comes to rescue.

# using property class
class Celsius:
    def __init__(self, temperature=0):
        self.temperature = temperature

    def to_fahrenheit(self):
        return (self.temperature * 1.8) + 32

    # getter
    def get_temperature(self):
        print("Getting value...")
        return self._temperature

    # setter
    def set_temperature(self, value):
        print("Setting value...")
        if value < -273.15:
            raise ValueError("Temperature below -273.15 is not possible")
        self._temperature = value

    # creating a property object
    temperature = property(get_temperature, set_temperature)


human = Celsius(37)

print(human.temperature)

print(human.to_fahrenheit())

human.temperature = -300

"""
As we can see, any code that retrieves the value of temperature will automatically call get_temperature()
instead of a dictionary (__dict__) look-up.

Similarly, any code that assigns a value to temperature will automatically call set_temperature().

We can even see above that set_temperature() was called even when we created an object.

human = Celsius(37) # prints Setting value...
Can you guess why?

The reason is that when an object is created, the __init__() method gets called. 
This method has the line self.temperature = temperature. This expression automatically calls set_temperature().

Similarly, any access like c.temperature automatically calls get_temperature(). This is what property does.
"""

"""
In Python, property() is a built-in function that creates and returns a property object. The syntax of this function is:

property(fget=None, fset=None, fdel=None, doc=None)
Here,

fget is function to get value of the attribute
fset is function to set value of the attribute
fdel is function to delete the attribute
doc is a string (like a comment)
"""


# Best practice to use property

# Using @property decorator
class Celsius:
    def __init__(self, temperature=0):
        self.temperature = temperature

    def to_fahrenheit(self):
        return (self.temperature * 1.8) + 32

    @property
    def temperature(self):
        print("Getting value...")
        return self._temperature

    @temperature.setter
    def temperature(self, value):
        print("Setting value...")
        if value < -273.15:
            raise ValueError("Temperature below -273 is not possible")
        self._temperature = value


# create an object
human = Celsius(37)

print(human.temperature)

print(human.to_fahrenheit())

coldest_thing = Celsius(-300)
