# Namespace is the area where we create and store variables/objects. Types are class and object/instance namespace.
class Computer:
    # Below variables are called as class/static variables and is common for all the objects of this class.
    # Can be accessed with object or by class name.
    # When updated through Class name, it will reflect in all the objects.
    # When updated through object, updates will be for particular object.

    processor_name = "Intel"

    def __init__(self, cpu, ram):
        # self holds the object created.Example:  c1 = Computer() , self will have c1.
        # Constructor allocates memory to object being created.
        # Memory consumed by objects depends upon number and type of member attributes.
        print(self)
        print(type(self))
        # Below variables are called as instance variable as they are specific to the instance of this class.
        self.cpu = cpu
        self.ram = ram
        self.have_webcam = True  # Default value of this class. But could be changes using . (dot)

    # About Methods: Accessor(Getters) and Mutator(Setters) methods.
    # Types of methods: Instance methods, class methods and static methods.
    # Below are instance methods i.e. they deal with instance variables. Take self (instance)
    def print_configuration(self):
        # self hold the object through which this method is called.
        # Could be called as c1.print_configuration(). => self will be c1
        # Or could be called as Computer.print_configuration(c1) => Here we explicitly defined c1 as self
        print(f"Crazy high specs are {self.processor_name} {self.cpu} {self.ram} {self.have_webcam}")

    def compare_machines(self, other):
        return self.ram == other.ram

    def update_ram(self, new_ram):
        self.ram = new_ram

    # Below are class methods i.e. they deal with class/static variables. Take cls (class reference)
    @classmethod
    def get_processor_name(cls):
        return cls.processor_name

    # Below are static methods i.e. doesn't deal with either instance variable or class variable.
    # They are meant to do something else. Doesn't take anything.
    @staticmethod
    def info_about_this_class():
        return "This is Computer class"


# Class method
print(Computer.get_processor_name())
# Static method
print(Computer.info_about_this_class())

comp1 = Computer("i5", "16")
comp2 = Computer("i7", "8")
# Instance methods
Computer.print_configuration(comp1)

# Direct updates
comp2.have_webcam = False
# comp2.print_configuration()
