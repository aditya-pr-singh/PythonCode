class Maths:
    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2
    def add(self):
        return self.num1+self.num2
        print("The sum of num1 and num2:",self.sum)
    def subt(self):
        return self.num1-self.num2
        print("The sub of num1 and num2 is:",self.sub)
    def mult(self):
        return self.num1*self.num2
        print("The mul of num1 and num2 is:",self.mul)
    def divi(self):
        return self.num1//self.num2
        print("The div of num1 and num2 is:",self.div)
c1=Maths(10,5)

print(c1.add())
print(c1.subt())
print(c1.mult())
print(c1.divi())