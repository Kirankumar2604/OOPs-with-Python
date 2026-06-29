# class Student:
#     def __init__(self,name):
#         self.name = name

# s1 = Student("kirankumar")
# print(s1.name)
# del s1.name
# print(s1)

# class Account:
#     def __init__(self,acc_no,acc_pass):
#         self.accno = acc_no
#         self.__accpass = acc_pass
#     def reset(self):
#         print(self.__accpass)

# a1 = Account("12HDFC34","4H3@2n1")
# print("Account number:",a1.accno,"Account Password:",a1.accpass)
# a1.reset()

class Person:
    __name = "kiran"
    def __greet(self, name):
        print("wellcome",name)
    def put(self):
        self.__greet("kiran")   

p1 = Person()
p1.put()
print(p1.__name())


        