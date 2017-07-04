import unittest
from Student import Student, PrimaryStudent, SecondaryStudent



class StudentTest(unittest.TestCase):

    def setUp(self):
        pass

    def test_primary_can_report_to_school(self):
        """location should be school after the report to school"""
        inno = PrimaryStudent("Innocent", "P1")
        inno.report_to_school()
        self.assertEqual("school", inno.location)

    def test_secondary_can_report_to_school(self):
        """location should be equal to school after the report to school method"""
        inno = SecondaryStudent("Innocent", "S1", "lion")
        inno.report_to_school()
        self.assertEqual("school", inno.location)

    def test_primary_can_go_to_class(self):
        """status should be "in class" after the go to class method for primary"""
        inno = PrimaryStudent("Innocent", "P1")
        inno.go_to_class()
        self.assertTrue(inno.status == "in class")

    def test_secondary_can_go_to_class(self):
        """status should be "in class" after the go_to_class method for secondary"""
        inno = SecondaryStudent("Innocent", "S1", "lion", True)
        inno.go_to_class()
        self.assertTrue(inno.status == "in class")

    def test_calculate_fees_primary(self):
        """calculate_fees should return 400 for primary"""
        inno = PrimaryStudent("Innocent", "P1" )
        inno_fees = inno.calculate_fees()
        self.assertEqual(inno_fees, 400)

    def test_calculate_fees_secondary_no_bus(self):
        """calculate_fees should return 400 with no bus fare """
        inno = SecondaryStudent("Innocent", "S1", "lion")
        inno_fees = inno.calculate_fees()
        self.assertEqual(inno_fees, 400)

    def test_calculate_fees_secondary_bus(self):
        """calculate_fees should return 500 if student uses bus"""
        inno = SecondaryStudent("Innocent", "S1", "lion", True)
        inno_fees = inno.calculate_fees()
        self.assertEqual(inno_fees, 500)

    def test_pay_fees_with_string_input(self):
        """pay_fees should raise type error for non-numeric input"""
        inno = SecondaryStudent("Innocent", "S1", "lion")
        self.assertRaises(TypeError, inno.pay_fees, '700')

    def test_pay_fees_success(self):
        """should change fees due attribute"""
        inno = PrimaryStudent("Innocent", "P1" )
        due_1 = inno._fees_due
        inno.pay_fees(300)
        due_2 = inno._fees_due
        self.assertEqual([due_1, due_2], [400, 100])

    def test_go_home_success(self):
        """location should be home after the go_home method for both primary and secondary"""
        student1 =  PrimaryStudent("Innocent", "P1")
        student2 =  SecondaryStudent("Asiimwe", "S1", "lion")
        student1.go_home()
        student2.go_home()
        self.assertEqual([student1.location, student2.location], ['home', 'home'])

    def test_go_to_detention_success(self):
        """for secondary students go_to_dention should change in_detention to true"""
        inno = SecondaryStudent("Innocent", "S1", "lion")
        before_detention = inno.detention
        inno.go_to_detention()
        after_detention = inno.detention
        self.assertEqual([before_detention, after_detention], [ False, True])

    def test_leave_detention(self):
        """when student leaves detention the in_detention should change to False"""
        inno = SecondaryStudent("Innocent", "S1", "lion")
        inno.go_to_detention()
        state1 = inno.detention
        inno.leave_detention()
        state2 = inno.detention
        self.assertEqual([state1, state2], [ True, False])
        