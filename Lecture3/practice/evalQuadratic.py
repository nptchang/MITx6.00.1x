a = -3.17
b = 1.47
c = -7.63
x = -0.39

def evalQuadratic(a, b, c, x):
    '''
    a, b, c: numerical values for the coefficients of a quadratic equation
    x: numerical value at which to evaluate the quadratic.
    '''
    return a*(x**2) + b*x + c

print (evalQuadratic(a, b, c, x))
