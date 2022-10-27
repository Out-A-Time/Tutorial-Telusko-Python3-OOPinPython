class Student:
    # Class attribute/variable
    school = "Telusko University"

    # Instance attribute/variable (can be used with instance methods)
    def __init__(self, m1, m2, m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def avg_grade(self):
        return (self.m1 + self.m2 + self.m3)/3

    # 'Getter' - Accessor Methods
    def get_m1(self):
        return self.m1

    # 'Setter' - Mutator Methods
    def set_m1(self, value):
        self.m1 = value

    @classmethod  # decorator
    def get_school(cls):
        return cls.school

    @staticmethod  # decorator
    def info():
        print('This is something something')


s1 = Student(34, 47, 32)
s2 = Student(89, 32, 12)

print(s1.avg_grade())
print(Student.get_school())
print(Student.info())
