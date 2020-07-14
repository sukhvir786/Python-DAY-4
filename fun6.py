#Compound Interest
import math
def FUN(p,r,t):
    AM = p*math.pow((1+(r/100)),t)
    CI = AM - p
    print("Amount : ",round(AM,2))
    print("Compound Interest : ",round(CI,2))

PRIN = float(input("Enter Principle : "))
RATE = float(input("Enter Rate : "))
TIME = float(input("Enter Time : "))
FUN(PRIN,RATE,TIME)