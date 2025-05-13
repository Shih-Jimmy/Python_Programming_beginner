class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname
        
    def printname(self):
        return f"My first name is {self.firstname} , my last name is {self.lastname}"
        
class Student(Person):
    pass

x = Student("Shih", "Jimmy")
print(x)
#print(x.firstname)
#print(x.lastname)
x.printname()
