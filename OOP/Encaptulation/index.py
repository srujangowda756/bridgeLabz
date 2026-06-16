class BankAccount:
    def __init__(self,balance):
        self.__balance = balance #private variable
    def get_balance(self):
        return self.__balance

class SavingsAccount(BankAccount):
    def __init__(self,balance,interest_rate):
        super().__init__(balance)
        self.interest_rate = interest_rate
    def calculate_interest(self):
        return self.get_balance() * self.interest_rate
s = SavingsAccount(1000, 0.05)
print("Balance:", s.get_balance())
print("Interest:", s.calculate_interest())


class Employee:
    def __init__(self, name, salary):
        self._name = name #protected variable
        self._salary = salary #protected variable

    def get_info(self):
        return f"Name: {self._name}, Salary: {self._salary}"


class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department
    def get_manager_info(self):
        return f"{self.get_info()}, Department: {self.department}"


m = Manager("Jane Smith", 70000, "Engineering")
print("Manager Info:", m.get_manager_info())