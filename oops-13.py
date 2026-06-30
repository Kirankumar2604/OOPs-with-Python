class employee:
    def __init__(self, role, depart, ctc):
        self.role = role
        self.depart = depart
        self.ctc = ctc

    def showDetail(self):
        print("Role:",self.role)
        print("Department:",self.depart)
        print("CTC:",self.ctc , "LPA")

class Engineer(employee):
    def __init__(self, name, age):
        self.name = name 
        self.age = age
        print("Name:",self.name)
        print("Age:",self.age)
        super().__init__("Engineer","IT",4)


emp = Engineer("Kiran Kumar G",21)
emp.showDetail()