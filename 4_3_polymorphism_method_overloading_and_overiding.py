class Student:
    """
    Method overloading (Compile time polymorphism) is a concept where multiple methods in the same class have the same name
    but differ in the number or types of parameters.
    Method overloading is not possible in python.
    Like you cannot have
    def add(a,b)
    def add(a, b, c)

    # But to still achieve this we do custom implementation
    """

    def add(self, a=None, b=None, c=None):
        if a and b and c:
            return a + b + c
        elif a and b and not c:
            return a + b
        else:
            return a


# Method overriding: When child class overrides method of super class.

class A:
    def show(self):
        print("show mwthod of class A")


class B(A):
    def show(self):
        print("show method of class B")


b = B()
b.show()
