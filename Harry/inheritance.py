class Employee:
    company='Collins'
    def __init__(self,name,dept):
        self.name=name
        self.dept=dept    
    
    def showDetails(self):
        print(f"Employee Name: {self.name}")
        print(f"Departmet: {self.dept}")

    def showComputerType(self):
        print("PC/Laptop")

class Developer(Employee):

    # def showComputerType(self):
    #     print("Macbook")

    def pl(self):
        print(f"{self.name}'s Programming Language is Python\nwho is working in {self.company} \nand department is {self.dept}.")
        
emp=Employee("Rajeev","PSW")
dev=Developer('Ranjan',"Digital")
# emp.pl()
dev.pl()
