class Car:
    @staticmethod
    def start():
        print("Started...")
    def Stop():
        print("Stoped...")

class BMW(Car):
    def __init__(self,name):
        self.name = name
        print(self.name)

brand = BMW("kirankumar")
brand.name
brand.start()

