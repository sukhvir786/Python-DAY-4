def FACT(n):
    if n == 0:
        return 1
    return n*FACT(n-1)
x = int(input("Factorial of : "))
print("Factorial of",x,"is : ",FACT(x))