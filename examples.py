# Inheritance
class Car(object): 
    def __init__(self):
        self.wheels = True
        self.needs_gas = True


class HatchBack(Car): 
    def __init__(self): 
        super(Car, self).__init__()
        self.hatchback_config = something_specific


# Composition
class BlackWheels(object):
    def __init__(self):
        self.color = black


class Car(object): 
    def __init__(self, wheels):
        self.wheels = wheels
        self.needs_gas = True


if __name__ == '__main__': 
    my_car = Car(
        wheels=BlackWheels()
    )

# Aggregation
class ClassRoom(object): 
    def __init__(self):
        self.students = set()

    def add_student(student): 
        self.students.add(student)

def Student(object): 
    def __init__(self, name, gender): 
        self.name = name
        self.gender = gender


if __name__ == '__main__': 
    classroom = ClassRoom()
    len(classroom.students) = 0 """True"""

    student_1 = Student(
        name='James',
        gender='male'
    )

    classroom.add_student(student_1)
    len(classroom.students) = 1 """True"""
