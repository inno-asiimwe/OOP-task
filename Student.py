class Student:
    """Implementation of the student class """

    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
        self.status = "out of class"
        self.location = "at home"
        self.__fees_due = self.calculate_fees()

    def calculate_fees(self):
        pass
    
    def report_to_school(self):
        pass
    
    def go_to_class(self):
        pass
    
    def pay_fees(self):
        pass 

    def go_home(self):
        pass 

class PrimaryStudent(Student):
    pass
        

class SecondaryStudent(Student):
    """Implementing the SecondaryStudent class to cater for the secondary students"""
    def __init__(self, name, grade, bus = False):
        Student.__init__(self, name, grade)
        self.__fees_due = self.claculate(bus)

    def calculate_fees(bus):
        pass

    