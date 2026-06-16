class Animal:
    def speak(self):
        pass
class Dog(Animal):
    def speak(self):
        return "Woof!"  
class Cat(Animal):
    def speak(self):
        return "Meow!"
animals = [Dog(), Cat()]
for animal in animals:
    print(animal.speak())

print("=========================================")

class Circle:
    def area(self, radius):
        return 3.14 * radius ** 2
class Square:
    def area(self, side):
        return side * side
def area_calculator(shape, value):
    return shape.area(value)

print("Circle Area:", area_calculator(Circle(), 5))
print("Square Area:", area_calculator(Square(), 4))

print("=========================================")

class Employee:
    def __init__(self, name):
        self.name = name
    def work(self):
        return f"{self.name} is working"
class Manager(Employee):
    def __init__(self, name):
        super().__init__(name)
    def work(self):
        super().work()  

e = Employee("Alice")
m = Manager("Bob")
print(e.work())
print(m.work())

