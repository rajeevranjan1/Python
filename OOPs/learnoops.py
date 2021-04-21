class Employee:
    company='Collins Aerospace'
    raiseAmount=1.04
    numberOfEmployees=0

    def __init__(self,first,last,pay):
        self.first=first
        self.last=last
        self.pay=pay
        self.email=self.first.lower()+'.'+self.last.lower()+'@'+self.company.split()[0].lower()+'.com'
        Employee.numberOfEmployees+=1
    
    def fullname(self):
        return f"{self.first} {self.last}"

    def applyRaise(self):
        self.pay=int(self.pay*self.raiseAmount)

    @classmethod
    def makeFromString(cls,string):
        first,last,pay=string.split('-')
        return cls(first,last,pay)

    @staticmethod
    def tagline():
        return 'alpha bravo collins'
    
    def __repr__(self):
        return f"Employee('{self.first}', '{self.last}',{self.pay})"

    def __str__(self):
        return f"{self.first} {self.last} - {self.email}"

class Developer(Employee):
    raiseAmount=1.10
    def __init__(self,first,last,pay,progLang):
        super().__init__(first,last,pay)
        self.progLang=progLang

class Manager(Employee):
    def __init__(self,first,last,pay,employee=None):
        super().__init__(first,last,pay)
        if employee is None:
            self.employee=[]
        else:
            self.employee=employee

    def addEmployee(self,emp):
        if emp not in self.employee:
            self.employee.append(emp)

    def removeEmployee(self,emp):
        if emp in self.employee:
            self.employee.remove(emp)

    def printEmployees(self):
        for emp in self.employee:
            print('-->',emp.fullname())
   
emp1=Employee('Ram','Kumar',10000)
emp2=Employee('Neha','Kumari',11000)
# emp3=Employee.makeFromString('firstname-lastname-50000')
dev1=Developer('Rajeev','Ranjan',50000,'Python')
dev2=Developer('Sohan','Das',60000,'Java')
mgr1=Manager('Manish','Malik',120000)
# mgr1.printEmployees()
mgr1.addEmployee(dev1)
# print(isinstance(dev1,Manager))
# print(isinstance(dev1,Employee))
# print(issubclass(Manager,Employee))
print(repr(mgr1))
print(int.__add__(1,4))



