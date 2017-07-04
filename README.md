# OOP-task
Modelling Students in a school using OOP principles (Day 2 task for Andela Self Learning Week)
Because of time constraints I use a very simplistic real life model of students in a school to demonstrate my understanding of OOP.

I demonstrate inheritance by the PrimaryStudent and SecondaryStudent classes inheriting from the parent class Student.
Methods report_to_school, go_to_class, leave_class, pay_fees and go_home are all implemented once in the parent class and inherite
by the child classes.

I demonstrate encapsulation by using a private variable _fees_due, which can be altered through the pay_fees method, I also implement a private method __expelled in the Student class. 

I demonstrate polymorphism by using and an abstract method calculate_fees which is defined in the parent class but implemented
by the child classes in different ways which also overriding. 

I use the SecondaryStudent class constructor to demonstrate overloading. SecondaryStudent("Innocent", "S1", "lion", True)
and SecondaryStudent("Asiimwe", "S5", "Tiger") are both valid calls to the constructor.

