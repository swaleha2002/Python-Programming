class Employee: 
    company =   "ITC"
    def show(self):
        print(f"The name is{self.name} and the salary is{self.salry}")
# class Programmer:
#     comapny = "ITC infotech"
#     def show(self):
#         print(f"The name is{self.name} and the salary is{self.salry}")
#     def showLanguage(self):
#         print(f"The name is{self.name} and the language is{self.language}")

class Programmer(Employee):
    comapny = "ITC infotech"
def showLanguage(self):
          print(f"The name is{self.name} and the language is{self.language}")
    
a = Employee()
b = Programmer()

print(a.company, b.comapny)
