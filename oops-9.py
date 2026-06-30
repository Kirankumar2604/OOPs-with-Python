#Class Method 

class Person:
    name = "oidoa"

    #static method 
    @staticmethod
    def ChangeName():
        print("kirankumar")
        
    #class methods (cls)
    @classmethod
    def ChangeName(cls,name):
        cls.name = name

    # instance method (self)
    # def ChangeName(self,name):
    #     self.__class__.name = name

p = Person()
p.ChangeName("kirankumar")
print(p.name)
print(Person.name)