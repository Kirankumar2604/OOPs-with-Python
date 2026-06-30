class complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img

    def showNum(self):
        print(self.real, "i +" , self.img,  "j")

    def __add__(self, obj):
        self.realNum = self.real + obj.real
        self.imgNum = self.img + obj.img
        return complex(self.realNum,self.imgNum)

    def __sub__(self, obj):
        self.realNum = self.real - obj.real
        self.imgNum = self.img - obj.img
        return complex(self.realNum,self.imgNum)

num1 = complex(2, 5)
num1.showNum()

num2 = complex(8, 3)
num2.showNum()

result = num2 + num1
result.showNum()

