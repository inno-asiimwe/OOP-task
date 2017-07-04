class Student:
    """Implementation of the student class """

    fee = 400

    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
        self.status = "out of class"
        self.location = "at home"

    def calculate_fees(self):
       raise NotImplementedError("implemented by child classes")
    
    def report_to_school(self):
        pass
    
    def go_to_class(self):
        pass
    
    def pay_fees(self):
        pass 

    def go_home(self):
        pass 

class PrimaryStudent(Student):
    """Implementing the PrimaryStudent class to cater for the primary stuents"""
    def __init__(self, name, grade):
        Student.__init__(self, name, grade)
        self.__fees_due = self.calculate_fees()

    def calculate_fees(self):
        return Student.fee 

class SecondaryStudent(Student):
    """Implementing the SecondaryStudent class to cater for the secondary students"""
    def __init__(self, name, grade, house, bus = False):
        Student.__init__(self, name, grade)
        self.house = house
        self.bus = bus
        self.__fees_due = self.calculate_fees()

    def calculate_fees(self):
        if self.bus:
            return Student.fee + 100
        else:
            return Student.fee

    