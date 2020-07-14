#definition of the function (formal parameters)
def SUM(x,y):
    s = 0
    for i in range(x,y+1):
        s = s + i
    print("Sum from",x,"to",y,"is:",s)
# function calling (actual parameters)
# actual parameters are also called arguments
SUM(12,93)
SUM(34,57)
SUM(15,27)
SUM(1,100)