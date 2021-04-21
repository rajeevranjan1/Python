class Main:
    def __init__(self,name):
        self.name=name

    def pr(self,msg):
        print(f"Main method: {msg}")

class SubClass(Main):
    def __init__(self,name):
        super().__init__(name)

    def pr(self,m):
        print(f"Subclass method: {m}")
        
b1=SubClass("Rajeev")
a1=Main("Ranjan")

print(issubclass(SubClass,Main))


