# Create a class “Programmer” for storing information of few programmers
# working at Microsoft.

class Programmer:
    company = "Microsoft"
    def __init__(self,name,salary,pin):
        self.name = name
        self.salary = salary
        self.pin = pin
p = Programmer ("Swaleha",150000,1234)
print(p.name,p.salary,p.pin,p.company)
p = Programmer ("Rohan",150000,1234)
print(p.name,p.salary,p.pin,p.company)