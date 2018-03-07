def iterPower(base, exp):
    result = 1
    for i in range(int(exp)):
        result = result * base
    return result

base = float(input("enter base: "))
exp = float(input("enter exp: "))
print (iterPower(base, exp))
