def gcdRecur(a,b):
    """
    a,b: positive integers
    returns: a positive integer, the greatest common divisor of a & b.
    """
    if b==0: return a
    elif a==0: return b
    else:
        return gcdRecur(b,a%b)

a = int(input("enter a: "))
b = int(input("enter b: "))
print (gcdRecur(a,b))
