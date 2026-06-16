from abc import ABC, abstractmethod, property

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

    def perimeter(self):
        return 2 * 3.14 * self.radius

c=Circle(5)
print("Circle Area:", c.area())
print("Circle Perimeter:", c.perimeter())

print("=========================================")

class laptop(ABC):
    @abstractmethod
    def get_model(self):
        pass

    @abstractmethod
    def get_price(self):
        pass

class Dell(laptop):
    def __init__(self, model, price):
        self.model = model
        self.price = price

    def get_model(self):
        return self.model

    def get_price(self):
        return self.price

d = Dell("Inspiron", 1000)
print("Dell Model:", d.get_model())
print("Dell Price:", d.get_price())

print("=========================================")

class Employee(ABC):
    @property
    @abstractmethod
    def name(self):
        pass

    @property
    @abstractmethod
    def salary(self):
        pass
class Manager(Employee):
    def __init__(self, name, salary):
        self._name = name
        self._salary = salary

    @property
    def name(self):
        return self._name

    @property
    def salary(self):
        return self._salary
m = Manager("Alice", 5000)
print("Manager Name:", m.name)  
print("Manager Salary:", m.salary)