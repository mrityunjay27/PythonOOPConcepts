# Polymorphism can be achieved via (One thing which will behave in different ways)
# 1. Duck Typing
# 2. Operator overloading
# 3. Method overloading
# 4. Method overriding

# Duck Typing
"""
Duck typing is a concept in programming where the type or class of an object is determined by its behavior
(methods and properties) rather than explicitly being checked.
The name comes from the saying, "If it looks like a duck, swims like a duck, and quacks like a duck,
then it probably is a duck." In other words, if an object can perform the required operations,
it can be treated as an instance of a particular type, regardless of what it actually is.

Duck typing is most commonly associated with dynamically typed languages like Python.
It allows for more flexible and reusable code because you don't have to explicitly declare the types of variables or function arguments.

Here's an example of duck typing in Python:

"""


class Duck:
    def quack(self):
        return "Quack quack"


class Dog:
    def quack(self):
        return "I'm quacking like a duck!"


def make_it_quack(duck):
    return duck.quack()


duck = Duck()
dog = Dog()

duck.quack()
dog.quack()

print(make_it_quack(duck))  # Outputs: Quack quack
print(make_it_quack(dog))  # Outputs: I'm quacking like a duck!

"""
In this example, both Duck and Dog have a quack() method, so make_it_quack() 
can operate on either, even though Dog is not a subclass of Duck. 
The function doesn't care about the actual class of the object—only that it has a quack() method. 
This is the essence of duck typing.
"""
