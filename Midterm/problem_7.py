def applyF_filterG(L, f, g):
    """
    Assumes L is a list of integers
    Assume functions f and g are defined for you.
    f takes in an integer, applies a function, returns another integer
    g takes in an integer, applies a Boolean function, returns either True or False
    Functions:
    1. Mutates L such that, for each element i originally in L, L contains
        i if g(f(i)) returns True, and no other elements
    2. Returns the largest element in the mutated L or -1 if the list is empty
    """
    NewL = []
    for i in L:
        if g(f(i)):
            NewL.append(i)
    L[:] = NewL
    if NewL == []:
        return -1
    else:
        Ans = 0
        for j in L:
            if j>0:
                Ans = j
        return Ans

def f(i):
    return i + 2
def g(i):
    return i > 5

L = [0, -10, 5, 6, -4]
print(applyF_filterG(L, f, g))
print(L)
