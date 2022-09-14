p=int(input("Enter the pricipal ammount:"))
r=int(input("enter intrest rate:"))
t=int(input("Enter number of time periods:"))
A=p*(1+r/100)**t
CI=A-p
print("Total compound intrest is:-",CI)

