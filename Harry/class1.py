class Emp:
    nom=10
    def __init__(self):
        print("Object Created")

employee=Emp()
employee.nom=12
print(employee.nom)
a=Emp()
print(a.nom)


