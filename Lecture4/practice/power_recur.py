def recurPower(base, exp):
    if exp==0:
        return 1
    elif exp==1:
        return base
    else:
        return base * recurPower(base, exp-1)

base = int(input("enter base: "))
exp = int(input("enter exp: "))
print (recurPower(base, exp))
