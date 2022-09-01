class Maths:
    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2
    def add(self):
        return self.num1+self.num2
    def subt(self):
        return self.num1-self.num2
    def mult(self):
        return self.num1*self.num2
    def divi(self):
        return self.num1//self.num2
c1=Maths(10,5)

print(c1.add())
print(c1.subt())
print(c1.mult())
print(c1.divi())