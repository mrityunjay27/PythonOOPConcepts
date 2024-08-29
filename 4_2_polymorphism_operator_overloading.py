
class Student:
    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2

    def __str__(self):
        return '{} {}'.format(self.m1, self.m2)

    def __add__(self, other):  # Magic Functions
        m1 = self.m1 + other.m1
        m2 = self.m2 + other.m2
        return Student(m1, m2)

    def __gt__(self, other):
        return self.m1 + self.m2 > other.m1 + other.m2

    @staticmethod
    def add_numbers():
        a = 5
        b = 5
        print(a + b)
        print(int.__add__(a, b))  # Behind the scenes


s1 = Student(90, 80)
s2 = Student(70, 50)

sum = s1 + s2  # -> Student.__add__(s1, s2)
print(sum)

print(s1 > s2)
