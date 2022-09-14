# p=int(input("Enter Principal Ammount: "))
# r=int(input("Enter rate: "))11
# t=int(input("Enter time "))
# SI=p*r*t/1000
# print("Total simple intrest is:-",SI)

from tokenize import Double


class intrest():
    def __init__(self,p,r,t):
        self.p=p
        self.r=r
        self.t=t
    def si(self):
        SI=self.p*self.r*self.t/100
        print(SI)
# p=int(input())
# r=int(input("Enter rate per year:"))
# t=int(input("Enter total time:"))
x,y,z = map(float,input("Enter Amount,Rate/y,time/y :-").split(","))
I1=intrest(x,y,z)
I1.si()