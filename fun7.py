#Factorial of a number
def FACT(n):
    f = 1
    for i in range(1,n+1):
        f = f * i
    print("factorial of",n,"is:",f)
x = int(input("Enter any integer value : "))
if x == 0:
    print("factorial of 0 is 1")
elif x<0:
    print("Kindly enter positive value")
else:
    FACT(x)
 