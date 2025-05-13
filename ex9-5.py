class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def myfunc(self):
        print("Hello my name is" + self.name + ",my age is " + str(self.age))
        # print("Hello my name is" + self.name + ",my age is " ,self.age)
        
p1 = Person("Jimmy",12)
print(p1)
p1.myfunc()
