class GrandFather:
    def land(self):
        return "Has 20 acres of land"
class Father(GrandFather):
    def business(self):
        return "Has a business"
class Son(Father):
    def car(self):
        return "Has a car"
s = Son()
print(s.land()) 
print(s.business())
print(s.car())

print("======================================================")

class Animal:
    def speak(self):
        return "Animal speaks"
class Dog(Animal):
    def speak(self):
        return "Dog barks"
class Puppy(Dog):
    def speak(self):
        return super().speak()
p = Puppy()
print(p.speak())

print("======================================================")

class A:
    def method_a(self):
        return "Method A from class A"
class B(A):
    def method_b(self):
        return "Method B from class B"
class C(B):
    def method_c(self):
        return "Method C from class C"
c = C()
print(c.method_a())
print(c.method_b())
print(c.method_c())

print("======================================================")

class Vehicle:
    def start_engine(self):
        return "Engine started"

class Car(Vehicle):
    def drive(self):
        return "Car is driving"

class BMW(Car):
    def drift(self):
        return "Drifting in BMW"

bmw = BMW()
print(bmw.start_engine())
print(bmw.drive())
print(bmw.drift())

print("======================================================")

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def get_info(self):
        return f"Name: {self.name} Age: {self.age}"
class Employee(Person):
    def __init__(self,name,age,employee_id):
        super().__init__(name,age)
        self.employee_id = employee_id
    
    def get_employee_info(self):
        return f"{self.get_info()} Employee ID: {self.employee_id}"
    
class Manager(Employee):
    def __init__(self,name,age,employee_id,department):
        super().__init__(name,age,employee_id)
        self.department = department
    
    def get_manager_info(self):
        return f"{self.get_employee_info()} Department: {self.department}"

m = Manager("Alice", 35, "E123", "Sales")
print(m.get_manager_info())
