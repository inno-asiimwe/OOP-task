# Object Oriented Programming in Python

Object Oriented Programming is a programming paradigm where programs are modelled into objects with properties and behaviour.
I will use this repository to explain the main concepts of OOP by modelling students in a simplistic school management system.

## Major Concepts of OOP
- Inheritance
- Encapsulation
- Abstraction
- Polymorphism

### Inheritance
This is the process where by a child(sub) class takes on attributes and methods of a parent(super) class.
The child(sub) class can override or extend the functionality of the parent(super) class. In the sample code `PrimaryStudent` and 
`SecondaryStudent` are subclasses of the `Student1 class. Due to inheritance most of the setter and getter methods will be implemented 
once in the Student class and inherited by the SecondaryStudent and PrimaryStudent classes.

### Encapsulation
Encapsulation also commonly known as `data hiding`, is a mechanism for restricting direct access to some of an object's data and methods. It will facilitate operations on the data. Only the object can interact with its internal private data. This helps prevent accidental manipulation of the data. In python there are really no `private` properties, generally `non-public` is preferred and the variables are preceeded with a double dashes or a single dash. The only difference between public and non-public attributes is that they non-public are not expected to be directly used by external parties and therefore can be changed or removed without worrying about backward compatibility. `firstname, lastname, and grade` attributes of the student class are `non-public` and as such they are only accessed through their getter and setter methods. Since its python they are still accessible by adding `__` at the beginning of the attribute name, in strictier languages it would not have been possible to access them directly outside the class.

### Abstraction
This is a mechanism of providing functionality to a user without revealing implementation details. An abstract class is a class with at least one abstract method, and an abstract method is one declared without being implemented. The abstract methods are implemented by the child classes. The `calculate_fees` method is abstract since it is defined in the Student class but not implemented. In turn it is implemented by each of the child classes. The fact that it can be called through the parent class reference literally makes it abstract to the caller.

### Polymorphism
This is a mechanism whereby an object takes on different forms depending on the data it is processing. Method overriding and Overloading are good examples for polymorphism. Also abstract classes support polymorphism. The `Student` class redefines the `__str__` method inherited from the `object` class. The `PrimaryStudent` and `SecondaryStudent` classes implement the inherited abstract method `calculate_fees` differently.

I use the SecondaryStudent class constructor to demonstrate overloading. SecondaryStudent("Innocent", "S1", "lion", True)
and SecondaryStudent("Asiimwe", "S5", "Tiger") are both valid calls to the constructor.

