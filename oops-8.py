class Car:
    def __init__(self,type):
        self.type = type
    
    @staticmethod
    def start():
        print("Started")

    @staticmethod
    def Stop():
        print("Stoped")

class Brand(Car):
    def __init__(self, type):
        super().__init__(type)

brd = Brand("SUV")
print(brd.type)
