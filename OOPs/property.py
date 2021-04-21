class Employee:

    def __init__(self,first,last):
        self.first=first
        self.last=last
    @property
    def email(self):
        if self.first==None and self.last==None:
            return 'No email for deleted Name!'
        return f"{self.first.lower()}.{self.last.lower()}@email.com"

    @email.setter
    def email(self,em):
        p1=em.split('@')
        f,l=p1[0].split('.')
        self.first=f.capitalize()
        self.last=l.capitalize()
        
    @property
    def fullname(self):
        return f"{self.first} {self.last}"

    @fullname.setter
    def fullname(self,name):
        self.first,self.last=name.split()

    @fullname.deleter
    def fullname(self):
        print('Deleted Name!')
        self.first=None
        self.last=None

emp1=Employee('Rajeev','Ranjan')
emp1.first='Neha'
print(emp1.email)
print(emp1.fullname)
del emp1.fullname
print(emp1.email)
print(emp1.fullname)
