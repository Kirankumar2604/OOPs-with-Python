class Student:  
    college_name = "Garden City University"
    def __init__(self, fullname, Totalmarks):
        self.name = fullname
        self.marks = Totalmarks
        print("Creating New Student Record")  

    def wellcome(self):
        print("wellcome student", self.name)
    def get_marks(self):
        return self.marks        
        
name = "kirankumar"
marks = 90
s1 = Student(name, marks)
# print("name:", s1.name)
# print("marks:",s1.marks)
print(s1.college_name)
s1.wellcome()
print("Student marks:",s1.get_marks())
print("==================")
name = "Dharshini"
marks = 99
s1 = Student(name, marks)
# print("name:",s1.name)
# print("marks:",s1.marks)
print(s1.college_name)
s1.wellcome()
print("Student marks:",s1.get_marks())