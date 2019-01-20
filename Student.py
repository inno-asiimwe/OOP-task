class Student:
    """Implementation of the student class """

    fees = 400

    def __init__(self, firstname, lastname, grade):
        self.set_firstname(firstname)
        self.set_lastname(lastname)
        self.set_grade(grade)

    def set_firstname(self, name):
        self.__firstname = name

    def set_lastname(self, name):
        self.__lastname = name

    def set_grade(self, grade):
        self.__grade = grade

    def get_firstname(self):
        return self.__firstname

    def get_lastname(self):
        return self.__lastname

    def get_grade(self):
        return self.__grade

    def calculate_fees(self):
        raise NotImplementedError("implemented by child classes")

    def __str__(self):
        return self.get_firstname() + " " + self.get_lastname()


class PrimaryStudent(Student):
    """
    Implementing the PrimaryStudent class
    to cater for the primary stuents
    """

    def __init__(self, firstname, lastname, grade):
        Student.__init__(self, firstname, lastname, grade)
        self.fees_due = self.calculate_fees()

    def calculate_fees(self):
        return Student.fees


class SecondaryStudent(Student):
    """
    Implementing the SecondaryStudent class
    to cater for the secondary students
    """
    def __init__(self, firstname, lastname, grade, house, bus=False):
        Student.__init__(self, firstname, lastname, grade)
        self.house = house
        self.bus = bus
        self.detention = False
        self.fees_due = self.calculate_fees()

    def calculate_fees(self):
        """Method calculates fees supposed to be paid by secondary student"""
        if self.bus:
            return Student.fees + 100
        return Student.fees

    def go_to_detention(self):
        """Method sets detention atttribute to True for seconary students"""
        self.detention = True

    def leave_detention(self):
        """ Method sets detention attribute to False
        as student leaves detention
        """
        self.detention = False
