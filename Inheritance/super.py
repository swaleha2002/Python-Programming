
class Employee:
     def __init__(self):
        print("Constructor of employee")
     a=1
class Programmer(Employee):
    def __init__(self):
        print("Constructor of employee")
    b=2
class Manager(Programmer):
    def __init__(self):
        super().__init__()
        print("Constructor of employee")
    c=3
o = Employee()
print(o.a)

o = Programmer
print(o.a,o.b)

o = Manager
print(o.a, o.b,o.c)
