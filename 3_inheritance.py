# Notes on inheritance.
# If a class's init method is found it will be called. Else it's parent's will be called if found.
# Method resolution order Left to Right
class A:

    def __init__(self):
        print("Creating object of class A")

    def feature1(self):
        print("Running feature 1 of A")

    def feature2(self):
        print("Running feature 2 of A")


class B(A):

    def __init__(self):
        super().__init__()  # Calling constructor of parent class.
        print("Creating object of class B")

    def feature3(self):
        print("Running feature 3 of B")

    def feature4(self):
        print("Running feature 4 of B")

    def feature1(self):  # Same name as parents method. This will be called.
        print("Running feature 1 of B")

    def explicit_call_of_feature1_from_class_A(self):
        super().feature1()


class C(B):
    # Though, it is just inheriting B, but it will have access of methods of both class B and A.

    def __init__(self):
        print("Creating object of class C")

    def feature5(self):
        print("Running feature 5 of C")

    def feature6(self):
        print("Running feature 6 of C")


class E:

    def __init__(self):
        print("Creating object of class E")

    def feature1(self):  # Same method.
        print("Running feature 1 of E")

    def feature8(self):
        print("Running feature 8 of E")


class MultipleInheritance(A, E):
    def __init__(self):
        super().__init__()  # A's will be called. Follows Left to Right. Method resolution order


a = A()
a.feature1()
a.feature2()

b = B()
b.feature1()  # Override in B, This will be called.
b.explicit_call_of_feature1_from_class_A()
b.feature2()
b.feature3()
b.feature4()

c = C()
c.feature1()  # Override in B, This will be called.
c.feature2()
c.feature3()
c.feature4()
c.feature5()
c.feature6()

mul = MultipleInheritance()  # Method resolution order.


