class Person:
    numberOfPeople = 0
    def __init__(self,name):
        self.name=name
        Person.addPeople()

    @classmethod
    def addPeople(cls):
        cls.numberOfPeople +=1

    # def __str__(self):
    #     return self.name
    
p1=Person("Rajeev")
p2=Person("Neha")
print(Person.numberOfPeople)



