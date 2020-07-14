"""
Problem:
    Heron's formula
    a,b,c are length of sides of a triangle 
    s = semi circumference
    s = (a+b+c)/2
    area = sqroot(s(s-a)(s-b)(s-c))
"""
# %%
def FUN():
    """ computes area of triangle using Heron's formula. """
    a = float(input("Enter length of side one: "))
    b = float(input("Enter length of side two: "))
    c = float(input("Enter length of side three: "))
    s = (a + b + c)/2
    AR = s*((s-a)*(s-b)*(s-c))
    print("Area of a triangle with sides",AR**0.5 )
# %%

