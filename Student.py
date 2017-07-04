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
    pass