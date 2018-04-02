def gcd(a, b):
    """
    a, b: two positive integers
    Returns the greatest common divisor of a and b
    """
    if a == 0:
        return b
    elif b == 0:
        return a
    elif a == b:
        return a
    elif a > b:
        return gcd(a%b, b)
    elif b > a:
        return gcd(a, b%a)

a = int(input("a: "))
b = int(input("b: "))
print(gcd(a, b))
