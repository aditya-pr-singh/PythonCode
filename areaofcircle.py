# r=int(input("Enter the radious of circle:-"))
# pie=3.14
# A=pie*(r)**2
# print(A)


class Cicle:
    def __init__(self,r):
        self.r=r
    
    def radius(self):
        pie=3.14
        return pie*self.r**2
c1=Cicle(int(input("enter radius  of circle:-")))
print(c1.radius())

