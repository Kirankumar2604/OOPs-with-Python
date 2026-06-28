class Car:
    def __init__(self):
        self.acc = False
        self.brk = False
        self.clutch = False

    def Start(self):
        self.clutch = True
        self.acc = True
        self.brk = False
        print("Car started.")

c1 = Car()
c1.Start()