#Inheritance is the capability of one class to derive 
#or inherit the properties from another class

class Person(object):
    def __init__(self,name,age,idnum) :
        self.name = name
        self.age = age
        self.idnum = idnum

        
    def myfunc(self):
        print(self.name)
        print(self.age)
        print(self.idnum)
    def details(self):
        print("My ame is ",self.name ," and my age is ",self.age,"and my id is ",self.idnum)
class Employee(Person):
    def __init__(self,name,age,idnum,salary):
        # invoking the __init__ of the parent class
        Person.__init__(self,name,age,idnum)
        self.salary = salary
    def myfunc(self):
        Person.myfunc(self)
        print(self.salary)
    def details(self):
        Person.details(self)
        print("My salary is ",self.salary)


emp1 = Employee('rahul',20,1234,20000)
emp1.myfunc()
emp1.details()