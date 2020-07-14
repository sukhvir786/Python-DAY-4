# Simple Interest
def FUN(p,r,t):
    SI = (p*r*t)/100
    AM = SI + p
    print("Simple Interest : ",round(SI,2))
    print("Amount : ",round(AM,2))

PRIN = float(input("Enter Principle : "))
RATE = float(input("Enter Rate : "))
TIME = float(input("Enter Time : "))
FUN(PRIN,RATE,TIME)
