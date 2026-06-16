class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        return f"{self.name} makes a sound"
    
class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)
    
    def speak(self):
        return f"{self.name} barks"
    
class Cat(Animal):
    def __init__(self, name):
        super().__init__(name)
    
    def speak(self):
        return f"{self.name} meows"

dog = Dog("Buddy")
cat = Cat("Whiskers")

print(dog.speak())
print(cat.speak())


print("======================================================")

class Vehicle:
    def __init__(self, brand):
        self.brand = brand
    
    def start(self):
        return f"{self.brand} is starting"
    
class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model
    
    def start(self):
        return f"{self.brand} {self.model} is starting"
    
class Bus(Vehicle):
    def __init__(self, brand, type):
        super().__init__(brand)
        self.type = type
    
    def start(self):
        return f"{self.brand} {self.type} is starting"

car = Car("Toyota", "Camry")
bus = Bus("Volvo", "Bus")

print(car.start())
print(bus.start())


print("======================================================")

class Shape:
    def __init__(self, color):
        self.color = color
    
    def area(self):
        return f"{self.color} shape"
    
class Circle(Shape):
    def __init__(self, color, radius):
        super().__init__(color)
        self.radius = radius
    
    def area(self):
        return f"{self.color} circle with radius {self.radius}"
    
class Rectangle(Shape):
    def __init__(self, color, width, height):
        super().__init__(color)
        self.width = width
        self.height = height
    
    def area(self):
        return f"{self.color} rectangle with width {self.width} and height {self.height}"

circle = Circle("Red", 5)
rectangle = Rectangle("Blue", 10, 20)

print(circle.area())
print(rectangle.area())

print("======================================================")

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    
    def work(self):
        return f"{self.name} is working"
    
class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department
    
    def work(self):
        return f"{self.name} is managing {self.department}"
    
class Developer(Employee):
    def __init__(self, name, salary, language):
        super().__init__(name, salary)
        self.language = language
    
    def work(self):
        return f"{self.name} is coding in {self.language}"

manager = Manager("John", 5000, "IT")
developer = Developer("Jane", 4000, "Python")

print(manager.work())
print(developer.work())

print("======================================================")

class BankAccount:
    def deposite(self):
        print("Depositing...")
    
    def withdraw(self):
        print("Withdrawing...")
    
    def check_balance(self):
        print("Checking balance...")

class SavingsAccount(BankAccount):
    pass

class CurrentAccount(BankAccount):
    pass


savings = SavingsAccount()
savings.withdraw()
savings.check_balance()

current = CurrentAccount()
current.withdraw()
current.check_balance()