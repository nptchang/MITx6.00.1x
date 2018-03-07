def square(x):
    """
    x: int or float.
    """
    return x**2



def fourthPower(x):
    """
    x: int or floar.
    """
    x=square(square(x))
    return x


x=int(input("enter x:"))
print (fourthPower(x))
