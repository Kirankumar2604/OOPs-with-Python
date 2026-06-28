class Student:
    @staticmethod #decorator
    def about():
        print("Creating a new method")
    
    def __init__(self, name, USN, marks):
        self.name = name
        self.usn = USN
        self.marks = marks

    def get_info(self):
        value = 0
        for value in self.marks:
            value += value
        print("hi", s1.name ,"your USN:",s1.usn,"avg score", value)

s1 = Student("Krian Kumar G","23BTCE130",[94,60,83])
s1.about()
s1.get_info()

s1.name = "Dharshini A"
s1.marks = [84,94,92]
s1.usn = "23BTCE120"
s1.get_info()
