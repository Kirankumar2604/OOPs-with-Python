class Circle:
    def __init__(self,r):
        self.r = r
        print("radius:",self.r)

    def area(self):
        return 3.14 * self.r ** 2

    def perimiter(self):
        return 2 * 31.4 * self.r
cr = Circle(4)
print(cr.area())
print(cr.perimiter())