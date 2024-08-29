class Student:

    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no
        self.laptop = self.Laptop("i5", 32)  # Here

    def get_student_info(self):
        print(f"{self.name} has Laptop with specs {self.laptop.cpu} {self.laptop.ram}")
        self.laptop.get_laptop_info()

# Concept of inner class.
# You can obliviously create instance of inner class inside outer class (see init)
# But also, you can create it outside outer class. Focus on how methods are being called.
    class Laptop:

        def __init__(self, cpu, ram):
            self.cpu = cpu
            self.ram = ram

        def get_laptop_info(self):
            print(f"{self.cpu} {self.ram}")


s1 = Student("Henry", 72)
s1.get_student_info()

l1 = Student.Laptop("i7", 64)
