def gcdIter(a,b):
    """
    a, b: positive integers
    returns: a positive integer, the greatest common divisor of a & b.
    """
    if a<b:
        testNum = a
    else:
        testNum = b

    while testNum > 1:
        if a%testNum==0 and b%testNum==0:
            break
        else:
            testNum = testNum-1
    return testNum

a = int(input("enter a: "))
b = int(input("enter b: "))
print (gcdIter(a,b))
