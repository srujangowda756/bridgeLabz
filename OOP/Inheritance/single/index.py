class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Student(Person):
    def __init__(self, id, name, age):
        super().__init__(name, age)
        self.id = id

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}, ID: {self.id}")

s=Student(12345, "John", 20)
s.display_info()


print("======================================================")

class Car:
    def __init__(self, typ):
        self.type = type

class BMW(Car):
    def __init__(self, type, model):
        super().__init__(type)
        self.model = model

    def display_info(self):
        print(f"Type: {self.type}, Model: {self.model}")
b = BMW("EV", "X5")
b.display_info()

print("======================================================")

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

class Developer(Employee):
    def __init__(self, name, salary, programming_language):
        super().__init__(name, salary)
        self.programming_language = programming_language

    def display_info(self):
        print(f"Name: {self.name}, Salary: {self.salary}, Programming Language: {self.programming_language}")

d = Developer("Alice", 50000, "Python")
d.display_info()

print("======================================================")

class Animal:
    def __init__(self, number_of_legs):
        self.number_of_legs = number_of_legs

class Dog(Animal):
    def __init__(self, number_of_legs, breed):
        super().__init__(number_of_legs)
        self.breed = breed

    def display_info(self):
        print(f"Number of Legs: {self.number_of_legs}, Breed: {self.breed}")
dog = Dog(4, "golden retriever")
dog.display_info()

print("======================================================")

class Shape:
    def __init__(self, color):
        self.color = color

class Circle(Shape):
    def __init__(self, color, radius):
        super().__init__(color)
        self.radius = radius

    def display_info(self):
        print(f"Color: {self.color}, Radius: {self.radius}")    
c = Circle("red", 5)
c.display_info()