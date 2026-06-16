class Basic_pay:
    def basic_pay(self):
        return 50000

class Bonus:
    def bonus(self):
        return 10000

class Total_salary(Basic_pay, Bonus):
    def total_salary(self):
        return self.basic_pay() + self.bonus()
t = Total_salary()
print(f"Total Salary: {t.total_salary()}")

print("======================================================")

class Camera:
    def click_photo(self):
        return "Capturing photo"
class telephone:
    def make_call(self):
        return "Making a call"
class Smartphone(Camera, telephone):
    def watch_movie(self):
        return "Watching a movie"
s = Smartphone()
print(s.click_photo())
print(s.make_call())
print(s.watch_movie())


print("======================================================")

class OnlineCourse:
    def course_content(self):
        return "Course content: Python programming"
class OfflineCourse:
    def course_content(self):
        return "Course content: Data Science"
class HybridCourse(OnlineCourse, OfflineCourse):
    def course_content(self):
        return super().course_content()

h = HybridCourse()
print(h.course_content())

print("======================================================")

class Printer:
    def print_document(self):
        return "Printing document"
class Scanner:
    def scan_document(self):
        return "Scanning document"
class SmartPrinter(Printer, Scanner):
    def copy_document(self):
        return "Copying document"
a = SmartPrinter()
print(a.print_document())
print(a.scan_document())
print(a.copy_document())

print("======================================================")

class Person:
    def __init__(self, name,age):
        self.name = name
        self.age = age
    
    def get_info(self):
        return f"Name: {self.name} Age: {self.age}"

class MedicalRecord:
    def __init__(self):
        self.records = []

    def add_record(self, record):
        self.records.append(record)
        return f"Adding medical record: {record}"
    
    def get_records(self):
        return f"Medical records: {', '.join(self.records)}"

class Insurance:
    def __init__(self,provider,coverage_amount):
        self.provider = provider
        self.coverage_amount = coverage_amount
    
    def check_coverage(self):
        if self.coverage_amount > 200000:
            return "NO coverage"
        elif self.coverage_amount > 100000:
            return "Partial coverage"
        else:
            return "Full coverage"

class Patient(Person, MedicalRecord, Insurance):
    def __init__(self, name, age, provider, coverage_amount):
        Person.__init__(self, name, age)
        Insurance.__init__(self, provider, coverage_amount)
        MedicalRecord.__init__(self)

p = Patient("John Doe", 30, "HealthCare Inc.", 150000)
print(p.get_info())
print(p.add_record("Diabetes"))
print(p.get_records())
print(p.check_coverage())