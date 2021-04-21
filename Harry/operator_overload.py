class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def details(self):
        return f"Name: {self.name}\nAge: {self.age}\n"

    def __add__(self,anotherPerson):
        return self.name +' '+anotherPerson.name

    def __str__(self):
        return self.details()

p1=Person('Rajeev',35)
p2=Person('Neha',29)
p3=Person('Chuhi',25)
print(p1+p2)