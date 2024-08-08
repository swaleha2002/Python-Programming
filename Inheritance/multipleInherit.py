class Employee: 
    company =   "ITC"
    name ="default"
    def show(self):
        print(f"The name is{self.name} and the salary is{self.company}")
class Coder:
    language = "Python"
    def printLanguage(self):
        print("out of all the languages here is your language :{self.language}")
    
class Programmer(Employee,Coder):
    company = "ITC infotech"
def showLanguage(self):
          print(f"The name is{self.company} and the language is{self.language}")
    
a = Employee()
b = Programmer()
b.show()
b.printLanguage()
# b.showLanguage()

