class Employee:
    'Documentation String.'
    rCount = 0
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        Employee.rCount += 1

    def output(self):
        print ("Name : " + str(self.name) + "\n" + "Age: " + str(self.age))



RecList = []

emp = Employee("Xavier", 24)
print (emp.rCount)
RecList.append(emp)
emp2 = Employee("Niki", 22)
RecList.append(emp2)
print (emp2.rCount)
emp3 = Employee("Luke", 23)
print (emp3.rCount)
RecList.append(emp3)

for i in RecList:
    print ("Employee.__doc__:", i.__doc__)
    print ("Employee.__name__:", i.__class__)
    print ("Employee.__module__:", i.__module__)
    #print ("Employee.__bases__:", i.__bases__)
    print ("Employee.__dict__:", i.__dict__)
    
