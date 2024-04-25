# inheritance
# wizard.py

class Wizard:
    def __init__(self, name):
        if not name:
            raise ValueError("Missing name")
        self.name = name

class Student(Wizard):
    def __init__(self, name, house):
        # call parent class __init__()
        super().__init__(name)
        self.house = house

class Professor(Wizard):
    # call parent class __init__()
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject

wizard = Wizard("Albus")
student = Student("Harry", "Gryffindor")
processor = Professor("Severus", "Defense Against the Dark Arts")