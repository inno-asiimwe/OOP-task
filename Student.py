class Student:
    """Implementation of the student class """

    fee = 400

    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
        self.status = "out of class"
        self.location = "home"
        self._fees_due = 0

    def calculate_fees(self):
       raise NotImplementedError("implemented by child classes")
    
    def report_to_school(self):
        self.location = "school"
    
    def go_to_class(self):
        """method changes status of student to in class """
        self.status = "in class"
    
    def leave_class(self):
        """Method changes status to out of class"""
        self.status = "out of class"
    
    def pay_fees(self,amount):
        """Method modifies the _fees_due attribute of the student object, returning a balance where applicable"""
        if self._fees_due == 0:
            return "no need for payment"
        elif amount > self._fees_due:
            self._fees_due = 0
            return amount - self._fees_due
        else:
            self._fees_due -= amount
        
    def go_home(self):
        """Method changes location attribute to home"""
        self.location = 'home'

class PrimaryStudent(Student):
    """Implementing the PrimaryStudent class to cater for the primary stuents"""
    def __init__(self, name, grade):
        Student.__init__(self, name, grade)
        self._fees_due = self.calculate_fees()

    def calculate_fees(self):
        return Student.fee 

class SecondaryStudent(Student):
    """Implementing the SecondaryStudent class to cater for the secondary students"""
    def __init__(self, name, grade, house, bus = False):
        Student.__init__(self, name, grade)
        self.house = house
        self.bus = bus
        self.detention = False
        self._fees_due = self.calculate_fees()

    def calculate_fees(self):
        """Method calculates fees supposed to be paid by secondary student"""
        if self.bus:
            return Student.fee + 100
        else:
            return Student.fee

    def go_to_detention(self):
        """Method sets detention atttribute to True for seconary students"""
        self.detention = True
    
    def leave_detention(self):
        """"Method sets detention attribute to False as student leaves detention"""
        self.detention = False

    