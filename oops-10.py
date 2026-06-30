class Student:
    def __init__(self,phy,maths,chem):
        self.phy = phy
        self.maths = maths
        self.chem = chem
        # self.percentage = str((self.phy + self.maths + self.chem) / 3) + " % "
    
    # def calcPercentage(self):
    #     self.percentage = str((self.phy + self.maths + self.chem) / 3) + " % "

    @property
    def percentage(self):
        return str((self.phy + self.maths + self.chem) / 3) + " % "



s1 = Student(90,97,88)
print(s1.percentage)
s1.phy = 100
s1.maths = 100
s1.chem = 99
print(s1.percentage)