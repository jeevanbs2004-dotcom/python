class Employee:
    def __init__(self, name, role):
        self.name = name
        self.role = role

    def display(self):
        print(self.name, "-", self.role)


class Trainer(Employee):
    def __init__(self, name, role, specialization):
        super().__init__(name, role)
        self.specialization = specialization

    def display(self):
        print(self.name, "-", self.role, "-", self.specialization)


class YogaInstructor(Employee):
    def __init__(self, name, role, yoga_style):
        super().__init__(name, role)
        self.yoga_style = yoga_style

    def display(self):
        print(self.name, "-", self.role, "-", self.yoga_style)


class MultiTrainer(Trainer, YogaInstructor):
    def __init__(self, name, role, specialization, yoga_style):
        Employee.__init__(self, name, role)
        self.specialization = specialization
        self.yoga_style = yoga_style

    def display(self):
        print(self.name, "-", self.role, "-", self.specialization, "-", self.yoga_style)


e = Employee("Alex", "Staff")
t = Trainer("Jordan", "Trainer", "Strength Training")
y = YogaInstructor("Maya", "Yoga Instructor", "Hatha Yoga")
m = MultiTrainer("Sam", "Multi Trainer", "Cardio", "Vinyasa Yoga")

e.display()
t.display()
y.display()
m.display()
